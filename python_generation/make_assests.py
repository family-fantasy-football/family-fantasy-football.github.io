from espn_api.football import League
import datetime
from typing import List, Tuple, Dict, Optional
import statistics
import numpy as np
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import math
import os
import subprocess
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os
import json
import matplotlib.pyplot as plt

from utils import *
from fetch import *

def generate_standings_table(league, through_week):
    def standings_table(league, through_week):
        standings_data = []
        teams = sorted(league.teams, key=lambda x: (x.wins, x.points_for), reverse=True)
        
        for team in teams:
            # Get last 3 results, pad with '' if less than 3 weeks
            recent_results = team.outcomes[:through_week][-3:]
            while len(recent_results) < 3:
                recent_results.insert(0, '')
                
            # Calculate win percentage for sorting
            games_played = team.wins + team.losses
            win_pct = team.wins / games_played if games_played > 0 else 0
                
            standings_data.append({
                'id': len(standings_data),
                'team': clean_team_name(team.team_name),
                'record': f"{team.wins}-{team.losses}",
                'record_sort': win_pct,  # Add sorting value
                'last3': ''.join(recent_results)
            })
        return standings_data

    os.makedirs("../assets/json", exist_ok=True)
    standings_json = standings_table(league, through_week)
    
    with open('../assets/json/standings.json', 'w') as f:
        json.dump(standings_json, f)
        
        
def save_team_logos(league):
    os.makedirs('assets/img', exist_ok=True)
    
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    for team in league.teams:
        if team.logo_url:
            driver.get(team.logo_url)
            driver.save_screenshot(f"../assets/img/{clean_team_name(team.team_abbrev)}_{league.year}.jpg")
            
    driver.quit()
    
def generate_roster_table(league, through_week):
    def roster_table(league, through_week):
        master_roster = []
        teams = league.teams
        
        for team in teams:
            all_players=[]
            for player in team.roster:
                if player.projected_total_points > 0.:
                    pct = player.total_points/(player.projected_total_points/17*through_week)*100
                    all_players.append({
                        "player_name": player.name,
                        "pos": player.position,
                        "total_points": f"{player.total_points:.2f}", 
                        "proj_points": f"{player.projected_total_points/17*through_week:.2f}",
                        "avg_points": f"{player.total_points/through_week:.2f}",
                        "pct_perform": f"{pct:.2f}" 
                    })
                else:
                    all_players.append({
                        "player_name": player.name,
                        "pos": player.position,
                        "total_points": f"{player.total_points:.2f}", 
                        "proj_points": f"{player.projected_total_points/17*through_week:.2f}",
                        "avg_points": f"{player.total_points/through_week:.2f}",
                        "pct_perform": "N/A" 
                    })
            master_roster.append(all_players)
        return master_roster

        
    os.makedirs("../assets/json/team_rosters", exist_ok=True)
    roster_json = roster_table(league, through_week)
    for team in league.teams:
        with open(f'../assets/json/team_rosters/{team.team_abbrev}_{league.year}.json', 'w') as f:
            json.dump(roster_json[team.team_id-1], f)
            
def create_weekly_position_rankings_json(teams, reg_season_length, box_scores, position):    
    weekly_rankings = []
    team_abbrevs = {team.team_name: team.team_abbrev for team in teams}
    for week in range(1, reg_season_length + 1):
        week_data = {}
        for team in teams:
            box = next((b for b in box_scores[week] 
                       if b.home_team == team or b.away_team == team), None)
            if box:
                lineup = box.home_lineup if box.home_team == team else box.away_lineup
                starters = {p.position: p.points for p in lineup 
                          if p.slot_position != 'BE' and p.slot_position != 'IR'}
                week_data[team.team_name] = starters
        
        pos_scores = {team_abbrevs[team]: data.get(position, 0) for team, data in week_data.items()}
        rankings = pd.Series(pos_scores).rank(ascending=False)
        for team, rank in rankings.items():
            weekly_rankings.append({
                'Week': week,
                'Team': team,
                'Rank': rank
            })
    
    df = pd.DataFrame(weekly_rankings)
    
    # Calculate average rank for each team for sorting
    avg_ranks = df.groupby('Team')['Rank'].mean().sort_values(ascending=False)
    sorted_teams = avg_ranks.index.tolist()
    
    # Create pivot table with sorted teams
    pivot_df = df.pivot_table(
        index='Team',
        columns='Week',
        values='Rank'
    ).reindex(sorted_teams)
    
    # Prepare data for ECharts
    echarts_data = []
    for y_index, team in enumerate(pivot_df.index):
        for x_index, week in enumerate(pivot_df.columns):
            value = pivot_df.iloc[y_index, x_index]
            if pd.notna(value):
                echarts_data.append([x_index, y_index, int(value)])

    # Truncate team names
    
    y_axis_labels = list(pivot_df.index)    
    echarts_config = {
        "grid": {
            "top": "10%",
            "bottom": "13%",
            "left": "10%",
            "right": "8%"
        },
        "xAxis": {
            "type": "category",
            "data": list(range(1, reg_season_length + 1)),
            "name": "Week",
            "nameLocation": "center",
            "nameGap": 35,
            "nameTextStyle": {
                "fontSize": 16
            },
            "axisLabel": {
                "fontSize": 14
            }
        },
        "yAxis": {
            "type": "category",
            "data": y_axis_labels,
            "name": "",
            "nameLocation": "end",
            "nameTextStyle": {
                "fontSize": 16
            },
            "axisLabel": {
                "fontSize": 14
            }
        },
        "visualMap": {
            "min": 1,
            "max": len(teams),
            "calculable": True,
            "orient": "vertical",
            "right": "right",
            "bottom": "30%",
            "text": [],
            "inRange": {
                "color": ["#4575b4", "#91bfdb", "#fee090", "#fc8d59", "#d73027"]
            }
        },
        "series": [{
            "type": "heatmap",
            "data": echarts_data,
            "label": {
                "show": True,
                "fontSize": 12
            }
        }]
    }

    with open(f"../assets/json/weekly_{position.lower()}_rankings.json", "w") as json_file:
        json.dump(echarts_config, json_file, indent=4)
    
    # return f"weekly_{position.lower()}_rankings.json"

def generate_echarts_heatmap_json(teams, box_scores, through_week):
    position_data = []
    for team in teams:
        positions = get_positional_scoring_amounts(box_scores, through_week, team)
        avg_points = {pos: sum(pts) / len(pts) if pts else 0 for pos, pts in positions.items()}
        avg_points['Team'] = team.team_name
        position_data.append(avg_points)
    
    df = pd.DataFrame(position_data)
    positions = get_non_flex_positions(box_scores,1)
    
    # Calculate ranks for all positions
    for position in positions:
        df[f"{position}_Rank"] = df[position].rank(ascending=False)
    
    # Prepare data for ECharts heatmap (x, y, value)
    echarts_data = []
    for y_index, team in enumerate(df['Team']):
        for x_index, position in enumerate(positions):
            rank = int(df[f"{position}_Rank"].iloc[y_index])
            echarts_data.append([x_index, y_index, rank])  # [x, y, rank]
    
    # Replace the lambda function with preprocessed data
    y_axis_labels = [team[:20] for team in df['Team']]  # Truncate long team names
    
    # Create ECharts JSON configuration
    echarts_config = {
        "grid": {
            "top": "10%",
            "bottom": "15%",
            "left": "20%",
            "right": "9%"
        },
        "xAxis": {
            "type": "category",
            "data": positions,
            "name": "Position",
            "nameLocation": "center",
            "nameTextStyle": {
                "fontSize": 16
            },
            "axisLabel": {
                "fontSize": 14
            }
        },
        "yAxis": {
            "type": "category",
            "data": y_axis_labels,  # Use preprocessed team names
            "name": "Team",
            "nameLocation": "end",
            "nameTextStyle": {
                "fontSize": 16
            },
            "axisLabel": {
                "fontSize": 14
            }
        },
        "visualMap": {
            "min": 1,
            "max": len(teams),
            "calculable": True,
            "orient": "vertical",
            "right": "right",
            "bottom": "30%",
            "text": [],
            "inRange": {
                "color": ["#4575b4", "#91bfdb", "#fee090", "#fc8d59", "#d73027"]  # Reverse the scale
            }
        },
        "series": [
            {
                "type": "heatmap",
                "data": echarts_data,
                "label": {
                    "show": True,
                    "fontSize": 12
                }
            }
        ]
    }
    
    # Save the JSON to a file
    with open("../assets/json/heatmap_config.json", "w") as json_file:
        json.dump(echarts_config, json_file, indent=4)
    
    # return "assets/heatmap_config.json"

def create_standings_bump_json(teams, through_week):
    weekly_standings = []
    
    # Generate unique colors for teams
    num_teams = len(teams)
    cmap = plt.get_cmap("tab20")
    colors = [cmap(i / num_teams) for i in range(num_teams)]
    color_hex = [f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}" for r, g, b, _ in colors]
    team_colors = {clean_team_name(team.team_name): color for team, color in zip(teams, color_hex)}
    
    # Process weekly standings
    for week in range(1, through_week + 1):
        week_records = [(clean_team_name(team.team_name), 
                        sum(1 for x in team.outcomes[:week] if x == 'W'),
                        sum(team.scores[:week])) 
                       for team in teams]
        sorted_teams = sorted(week_records, key=lambda x: (-x[1], -x[2]))
        
        for rank, (team_name, wins, points) in enumerate(sorted_teams, 1):
            weekly_standings.append({
                'Week': week,
                'Team': team_name,
                'Rank': rank
            })
    
    # Create ECharts series data
    series_data = []
    team_names = sorted(set(item['Team'] for item in weekly_standings))
    
    for team in team_names:
        team_data = [item['Rank'] for item in weekly_standings if item['Team'] == team]
        series_data.append({
            'name': team,
            'type': 'line',
            'smooth': True,
            'lineStyle': {
                'width': 3,
                'color': team_colors[team]
            },
            'itemStyle': {
                'color': team_colors[team]
            },
            'data': team_data,
            'symbol': 'circle',
            'symbolSize': 12,
            'label': {
                'show': False,
                'position': 'right',
                'formatter': team if len(team) < 15 else f"{team[:12]}..."
            }
        })

    # Create the complete ECharts option
    echarts_option = {
        'title': {
            'text': 'Team Rankings Over Time',
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{a}<br/>Week {b}: Rank {c}'
        },
        'xAxis': {
            'type': 'category',
            'name': 'Week',
            'nameLocation': 'middle',
            'nameGap': 30,
            'data': list(range(1, through_week + 1))
        },
        'yAxis': {
            'type': 'value',
            'name': 'Rank',
            'nameLocation': 'middle',
            'nameGap': 20,
            'inverse': True,
            'min': 1,
            'max': len(teams)
        },
        'series': series_data,
        "grid": {
        "left": "8%",
        "right": "0%",
        "bottom": "10%",
        "top": "10%",
        "containLabel": True
        }
    }
    
    with open('../assets/json/bump_chart_data.json', 'w') as f:
        json.dump(echarts_option, f, indent=2)
    
    # return 'bump_chart_data.json'