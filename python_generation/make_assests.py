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
            "left": "5%",
            "right": "0%"
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
            "show": False,
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
        avg_points['Team'] = team.team_abbrev
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
            "left": "5%",
            "right": "0%"
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
            "show": False,
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
            'text': 'Standings Over Time',
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
        "left": "1%",
        "right": "0%",
        "bottom": "1%",
        "top": "10%",
        "containLabel": True
        }
    }
    
    with open('../assets/json/bump_chart_data.json', 'w') as f:
        json.dump(echarts_option, f, indent=2)
    
    # return 'bump_chart_data.json'
    
    
def generate_team_json(league, teams, box_scores_dict, reg_season_length, trades, transactions):
    """Generate JSON files for each team's data"""
    output_folder="../assets/json/team_data"
    os.makedirs(output_folder, exist_ok=True)
    draft_results = league.draft 
    drafted_players, all_value_diffs = get_drafted_player_data(reg_season_length, trades, league, transactions, draft_results)
    mean_value_diff = np.mean(all_value_diffs)
    std_value_diff = np.std(all_value_diffs)

    
    for team in teams:
        # Get team stats
        outcomes = team.outcomes[:reg_season_length]
        scores = team.scores[:reg_season_length]
        schedule = team.schedule[:reg_season_length]
        mov = team.mov[:reg_season_length]
        
        weekly_effs, total_bench_points, total_optimal_points, total_actual_points = get_efficiencies(
            reg_season_length, box_scores_dict, team)
        
        expected_wins, actual_wins, luck_factor, close_wins, close_losses = get_luck_values(
            team, outcomes, mov, teams, reg_season_length)
        
        longest_win_streak, longest_lose_streak, current_streak, streak_type = get_streaks(outcomes)
        
        # Create team summary data
        team_summary = [
            {"category": "Record", "value": f"{team.wins}-{team.losses}-{team.ties}"},
            {"category": "Points For", "value": f"{team.points_for:.2f}"},
            {"category": "Avg Points For", "value": f"{team.points_for/reg_season_length:.2f}"},
            {"category": "Points Against", "value": f"{team.points_against:.2f}"},
            {"category": "Avg Points Against", "value": f"{team.points_against/reg_season_length:.2f}"},
            {"category": "Points Left on Bench", "value": f"{total_bench_points:.2f}"},
            {"category": "Efficiency", "value": f"{total_actual_points/total_optimal_points*100:.2f}%"},
            {"category": "Current Streak", "value": f"{current_streak} {streak_type}"},
            {"category": "Longest Win Streak", "value": str(longest_win_streak)},
            {"category": "Longest Losing Streak", "value": str(longest_lose_streak)},
            {"category": "Expected Wins", "value": f"{expected_wins:.1f}"},
            {"category": "Actual Wins", "value": str(actual_wins)},
            {"category": "Luck Factor", "value": f"{luck_factor:.1f}"},
            {"category": "Close Games", "value": f"{close_wins}-{close_losses}"},
            {"category": "Season Pattern", "value": "".join(outcomes)}
        ]
        
        # Save team summary
        filename = f"{clean_team_name(team.team_abbrev).replace(' ', '_')}_{league.year}_summary.json"
        with open(os.path.join(output_folder, filename), 'w') as f:
            json.dump(team_summary, f, indent=2)
        
        # Generate positional stats
        positions = get_positional_scoring_amounts(box_scores_dict, reg_season_length, team)
        pos_stats = []
        act_pos = get_non_flex_positions(box_scores_dict,1)
        for pos in act_pos:
            scores = positions[pos]
            if scores:
                pos_stats.append({
                    "position": pos,
                    "average": round(sum(scores) / len(scores), 1),
                    "highest": round(max(scores), 1),
                    "lowest": round(min(scores), 1)
                })
        
        # Save positional stats
        pos_filename = f"{clean_team_name(team.team_abbrev).replace(' ', '_')}_{league.year}_positions.json"
        with open(os.path.join(output_folder, pos_filename), 'w') as f:
            json.dump(pos_stats, f, indent=2)
            
        
        weekly_data = []
        for week, eff in enumerate(weekly_effs, 1):
            weekly_data.append({
                "week": f"Week {week}",
                "efficiency": f"{eff:.1f}%"
            })

        # Save weekly efficiency data
        weekly_filename = f"{clean_team_name(team.team_abbrev).replace(' ', '_')}_{league.year}_weekly_eff.json"
        with open(os.path.join(output_folder, weekly_filename), 'w') as f:
            json.dump(weekly_data, f, indent=2)
            
            
        team_draft = []
        team_players = [player for player in drafted_players if player["drafted_team_id"] == team.team_id]

        for player in team_players:
            pick_grade = grade_pick(player['value_diff'], mean_value_diff, std_value_diff)
            team_draft.append({
                "team": player['drafted_team'].team_name,
                "round": player['round_num'],
                "pick": player['round_pick'],
                "player_name": player['player_name'],
                "points": f"{player['total_points']:.1f}",
                "before_trade": f"{player['points_before_leave']:.1f}",
                "after_trade": f"{player['points_after_trade']:.1f}",
                "draft_position": player['draft_position'],
                "value_diff": f"{player['value_diff']:.1f}",
                "grade": pick_grade
                })
                
        draft_filename = f"{clean_team_name(team.team_abbrev).replace(' ', '_')}_{league.year}_draft.json"
        with open(os.path.join(output_folder, draft_filename), 'w') as f:
            json.dump(team_draft, f, indent=2)
            
        # In generate_team_data_json, add:
        scores = team.scores[:reg_season_length]
        outcomes = team.outcomes[:reg_season_length]
        schedule = team.schedule[:reg_season_length]
        opponent_stats = get_records_against(schedule, scores, outcomes)

        h2h_data = []
        for opp_id, stats in opponent_stats.items():
            opp_team = next(t for t in teams if t.team_id == opp_id)
            wins = stats['wins']
            losses = stats['games'] - stats['wins']
            avg_pf = stats['points_for'] / stats['games']
            avg_pa = stats['points_against'] / stats['games']
            
            h2h_data.append({
                "opponent": clean_team_name(opp_team.team_name),
                "record": f"{wins}-{losses}",
                "points": f"{avg_pf:.1f}-{avg_pa:.1f}"
            })

        # Save head to head data
        h2h_filename = f"{clean_team_name(team.team_abbrev).replace(' ', '_')}_{league.year}_h2h.json"
        with open(os.path.join(output_folder, h2h_filename), 'w') as f:
            json.dump(h2h_data, f, indent=2)    
        

def generate_weekly_scores_json(teams, reg_season_length, league):
    """Generate JSON for weekly scores line graph including league averages"""
    output_folder="../assets/json/team_data"
    os.makedirs(output_folder, exist_ok=True)
    
    # First calculate league average scores for each week
    league_avg_for = []
    
    for week in range(reg_season_length):
        week_scores = []
        for team in teams:
            if week < len(team.scores):
                week_scores.append(team.scores[week])

        
        # Calculate averages for the week
        avg_score = sum(week_scores) / len(week_scores) if week_scores else 0
        
        league_avg_for.append(round(avg_score, 1))
    
    # Generate eCharts data for each team
    for team in teams:
        echarts_data = {
            "tooltip": {
                "trigger": "axis"
            },
            "legend": {
                "data": ["Points For", "Points Against", "League Avg"]
            },
            "grid": {
                "top": "10%",
                "bottom": "5%",
                "left": "6%",
                "right": "0%"
            },
            "xAxis": {
                "type": "category",
                "data": [f"Week {w+1}" for w in range(reg_season_length)]
            },
            "yAxis": {
                "type": "value",
                "name": "Points",
                "nameLocation": "center",
                "nameGap": 35,
                "nameTextStyle": {
                    "fontSize": 16
                },
                "axisLabel": {
                    "fontSize": 14
                },
            },
            "series": [
                {
                    "name": "Points For",
                    "type": "line",
                    "data": [round(score, 1) for score in team.scores[:reg_season_length]],
                    "symbol": "circle",
                    "symbolSize": 8,
                    "lineStyle": {
                        "width": 3
                    }
                },
                {
                    "name": "Points Against",
                    "type": "line",
                    "data": [round(team.schedule[w].scores[w], 1) for w in range(reg_season_length)],
                    "symbol": "circle",
                    "symbolSize": 8,
                    "lineStyle": {
                        "width": 3
                    }
                },
                {
                    "name": "League Avg",
                    "type": "line",
                    "data": league_avg_for,
                    "symbol": "none",
                    "lineStyle": {
                        "type": "dashed",
                        "width": 2
                    }
                },
            ]
        }
        
        # Save team's weekly data
        filename = f"../assets/json/team_data/{clean_team_name(team.team_abbrev).replace(' ', '_')}_{league.year}_weekly_scores.json"
        with open(filename, 'w') as f:
            json.dump(echarts_data, f, indent=2)
            


def combine_draft_json():
    folder_path = "../assets/json/team_data/"
    output_file = "../assets/json/team_data/draft_total_2024.json"
    combined_data = []

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file ends with '_2024_draft.json'
        if file_name.endswith('_2024_draft.json'):
            file_path = os.path.join(folder_path, file_name)
            # Load JSON data
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if isinstance(data, list):
                    combined_data.extend(data)  # Add list data to combined data
                else:
                    raise ValueError(f"File {file_name} does not contain a list of records.")

    # Sort the combined data by the specified column
    sorted_data = sorted(combined_data, key=lambda x: x["draft_position"])

    # Save the sorted data to a new JSON file
    with open(output_file, 'w') as out_file:
        json.dump(sorted_data, out_file, indent=2)
