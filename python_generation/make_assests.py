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
            
def create_weekly_position_rankings_json(teams, week, box_scores, position):    
    weekly_rankings = []
    team_abbrevs = {team.team_name: team.team_abbrev for team in teams}
    for week in range(1, week + 1):
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
            "right": "0%",
            "containLabel": True
        },
        "xAxis": {
            "type": "category",
            "data": list(range(1, week + 1)),
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


def generate_echarts_heatmap_weekly_json(teams, box_score, week):
    positions = {'QB': [], 'RB': [], 'WR': [], 'TE': [], 'D/ST': [], 'K': []}
    position_data = []
    for team in teams:
        box_scores = box_score[week]
        box = next((b for b in box_scores if b.home_team == team or b.away_team == team), None)
        if box:
            lineup = box.home_lineup if box.home_team == team else box.away_lineup
            starters = [p for p in lineup if p.slot_position != 'BE' and p.slot_position != 'IR']
            for player in starters:
                if player.position in positions:
                    positions[player.position].append(player.points)
        positions =  {pos: scores for pos, scores in positions.items() if scores}          
        points = {pos: sum(pts) / len(pts) if pts else 0 for pos, pts in positions.items()}
        points['Team'] = team.team_abbrev
        position_data.append(points)
    
    df = pd.DataFrame(position_data)
    positions = get_non_flex_positions(box_score,1)
    
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
            "right": "0%",
            "containLabel": True
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
    with open("../assets/json/weekly_heatmap_config.json", "w") as json_file:
        json.dump(echarts_config, json_file, indent=4)


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
            "right": "0%",
            "containLabel": True
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
    
    
def generate_team_json(league, teams, box_scores_dict, week, trades, transactions):
    """Generate JSON files for each team's data"""
    output_folder="../assets/json/team_data"
    os.makedirs(output_folder, exist_ok=True)
    draft_results = league.draft 
    drafted_players, all_value_diffs = get_drafted_player_data(week, trades, league, transactions, draft_results)
    mean_value_diff = np.mean(all_value_diffs)
    std_value_diff = np.std(all_value_diffs)

    
    for team in teams:
        # Get team stats
        outcomes = team.outcomes[:week]
        scores = team.scores[:week]
        schedule = team.schedule[:week]
        mov = team.mov[:week]
        
        weekly_effs, total_bench_points, total_optimal_points, total_actual_points = get_efficiencies(
            week, box_scores_dict, team)
        
        expected_wins, actual_wins, luck_factor, close_wins, close_losses = get_luck_values(
            team, outcomes, mov, teams, week)
        
        longest_win_streak, longest_lose_streak, current_streak, streak_type = get_streaks(outcomes)
        
        # Create team summary data
        team_summary = [
            {"category": "Record", "value": f"{team.wins}-{team.losses}-{team.ties}"},
            {"category": "Points For", "value": f"{team.points_for:.2f}"},
            {"category": "Avg Points For", "value": f"{team.points_for/week:.2f}"},
            {"category": "Points Against", "value": f"{team.points_against:.2f}"},
            {"category": "Avg Points Against", "value": f"{team.points_against/week:.2f}"},
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
        positions = get_positional_scoring_amounts(box_scores_dict, week, team)
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
        scores = team.scores[:week]
        outcomes = team.outcomes[:week]
        schedule = team.schedule[:week]
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
        

def generate_weekly_scores_json(teams, week, league):
    """Generate JSON for weekly scores line graph including league averages"""
    output_folder="../assets/json/team_data"
    os.makedirs(output_folder, exist_ok=True)
    
    # First calculate league average scores for each week
    league_avg_for = []
    
    for week in range(week):
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
                "data": [f"Week {w+1}" for w in range(week)]
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
                    "data": [round(score, 1) for score in team.scores[:week]],
                    "symbol": "circle",
                    "symbolSize": 8,
                    "lineStyle": {
                        "width": 3
                    }
                },
                {
                    "name": "Points Against",
                    "type": "line",
                    "data": [round(team.schedule[w].scores[w], 1) for w in range(week)],
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

  
        
def create_weekly_scores_boxplot_json(teams, through_week, output_dir: str = "../assets/json"):
    boxplot_data = {
        "title": {
            "text": "Weekly Score Distribution by Team",
            "left": "center"
        },
        "xAxis": {
            "type": "category",
            "name": "Teams",
            "nameLocation": "middle",
            "nameGap": 30,
            "data": [team.team_abbrev for team in teams]
        },
        "yAxis": {
            "type": "value",
            "name": "Points Scored",
            "nameLocation": "middle",
            "nameGap": 30
        },
        "series": [
            {
                "name": "Weekly Scores",
                "type": "boxplot",
                "data": [],
                "itemStyle": {
                    "borderWidth": 2
                }
            },
            {
                "name": "All Scores",
                "type": "scatter",
                "data": []
            }
        ],
        "grid": {
            "left": "4%",
            "right": "1%",
            "bottom": "1%",
            "top": "10%",
            "containLabel": True
        }
    }
    
    # Calculate box plot data and gather all scores
    for idx, team in enumerate(teams):
        scores = team.scores[:through_week]
        
        # Calculate statistics
        q1 = np.percentile(scores, 25)
        median = np.percentile(scores, 50)
        q3 = np.percentile(scores, 75)
        iqr = q3 - q1
        lower_fence = max(min(scores), q1 - 1.5 * iqr)
        upper_fence = min(max(scores), q3 + 1.5 * iqr)
        
        # Add box plot data
        boxplot_data["series"][0]["data"].append([
            round(lower_fence, 2),
            round(q1, 2),
            round(median, 2),
            round(q3, 2),
            round(upper_fence, 2)
        ])
        
        # Add all scores as scatter points
        for score in scores:
            boxplot_data["series"][1]["data"].append([
                idx,            # x-coordinate (team index)
                round(score, 2),  # y-coordinate (score)
                team.team_abbrev  # name for tooltip
            ])
    
    os.makedirs(f"{output_dir}/plots", exist_ok=True)
    with open(f"{output_dir}/plots/boxplot_data.json", 'w') as f:
        json.dump(boxplot_data, f, indent=2)
        
def create_team_scatter_json(league, through_week, output_dir: str = "../assets/json"):
    # Get team data
    points_for = []
    points_against = []
    for team in league.teams:
        pf = sum(team.scores[:through_week])
        pa = sum(opponent.scores[i] for i, opponent in enumerate(team.schedule[:through_week]))
        points_for.append(pf)
        points_against.append(pa)

    # Calculate ranges and averages
    min_val = round(min(min(points_for), min(points_against)) - 150,0)
    max_val = round(max(max(points_for), max(points_against)) + 150,0)
    avg_pf = np.mean(points_for)
    avg_pa = np.mean(points_against)

    scatter_data = {
        "title": {
            "text": "Points For vs Points Against",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item",
            "formatter": "{b}"
        },
        "xAxis": {
            "type": "value",
            "name": "Points For",
            "nameLocation": "middle",
            "nameGap": 30,
            "min": min_val,
            "max": max_val
        },
        "yAxis": {
            "type": "value",
            "name": "Points Against",
            "nameLocation": "middle",
            "nameGap": 40,
            "min": min_val,
            "max": max_val
        },
        "series": [
            {
                "name": "Teams",
                "type": "scatter",
                "symbolSize": 15,
                "data": [
                    {
                        "name": clean_team_name(team.team_name),
                        "value": [round(pf, 2), round(pa, 2)]
                    }
                    for team, pf, pa in zip(league.teams, points_for, points_against)
                ],
                "label": {
                    "show": True,
                    "position": "top",
                    "formatter": "{b}"
                }
            },
            {
                "name": "Diagonal",
                "type": "line",
                "lineStyle": {
                    "type": "dashed",
                    "color": "gray"
                },
                "showSymbol": False,
                "data": [[min_val, min_val], [max_val, max_val]]
            },
            {
                "name": "Average Lines",
                "type": "line",
                "markLine": {
                    "silent": True,
                    "data": [
                        {
                            "xAxis": round(avg_pf, 2),
                            "lineStyle": {"color": "blue", "opacity": 0.5}
                        },
                        {
                            "yAxis": round(avg_pa, 2),
                            "lineStyle": {"color": "red", "opacity": 0.5}
                        }
                    ]
                }
            }
        ],
        "grid": {
            "left": "0%",
            "right": "5%",
            "bottom": "10%",
            "top": "10%",
            "containLabel": True
        }
    }
    
    os.makedirs(f"{output_dir}/plots", exist_ok=True)
    with open(f"{output_dir}/plots/scatter_data.json", 'w') as f:
        json.dump(scatter_data, f, indent=2)
        
def generate_best_pickups_json(league, waiver_adds, fa_adds, trades):
   """Process best FA/waiver pickups and save as JSON"""
   pickups = get_best_acquisitions(league, waiver_adds, fa_adds, trades)
   pickups.sort(key=lambda x: x['new_avg'], reverse=True)
   top_5 = pickups[:5]
   
   table_data = []
   for p in top_5:
       # Check if pickup came from waiver activities
       acquisition_type = "WAIVER" if any(p['player_name'] in str(w) for w in waiver_adds) else "FA"
       
       entry = {
           "team": p["team"],
           "week": p["week"], 
           "player_name": p["player_name"],
           "position": p["position"],
           "points_before": f"{p['prev_avg']:.1f}",
           "points_after": f"{p['new_avg']:.1f}",
           "points_diff": f"{p['improvement']:.1f}",
           "num_weeks_before": p["num_weeks_before"],
           "num_weeks_after": p["num_weeks_after"],
           "type": acquisition_type
       }
       table_data.append(entry)
       
   with open(f"../assets/json/transactions/best_fa_{league.year}.json", 'w') as f:
       json.dump(table_data, f, indent=1)
       
def generate_all_transactions_json(league, waiver_adds, fa_adds):
   transactions = []
   
   # Process all waiver/FA transactions
   for activity in (waiver_adds + fa_adds):
       for team, action, player_, bid in activity.actions:
           player = league.player_info(playerId=player_.playerId)
           acquisition_type = "WAIVER" if "WAIVER" in action else "FA"
           
           trans = {
               "team": clean_team_name(team.team_name),
               "week": week_of_transaction(activity.date),
               "player_name": player.name,
               "position": player.position,
               "type": acquisition_type,
               "bid_amount": bid if bid else 0
           }
           transactions.append(trans)
           
   # Sort by week
   transactions.sort(key=lambda x: x['week'])
   
   with open(f"../assets/json/transactions/all_fa_{league.year}.json", 'w') as f:
       json.dump(transactions, f, indent=1)

def generate_trades_json(league, trades):
   all_trades = []
   
   for trade in trades:
       trade_week = week_of_transaction(trade.date)
       teams = list(set([t for t, action, p, _ in trade.actions if action == 'TRADED']))
       
       # Only track trades from perspective of first team
       team_1, team_2 = teams[0], teams[1]
       team_1_players = []
       team_2_players = []
       
       for team, action, player_, _ in trade.actions:
           if action == 'TRADED':
               player = league.player_info(playerId=player_.playerId)
               if team == team_1:
                   team_1_players.append(player)
               else:
                   team_2_players.append(player)
       
       trade_entry = {
           "team_1": clean_team_name(team_1.team_name),
           "team_2": clean_team_name(team_2.team_name), 
           "week": trade_week,
           "team_1_sending": [f"{p.name} ({p.position})" for p in team_1_players],
           "team_2_sending": [f"{p.name} ({p.position})" for p in team_2_players]
       }
       all_trades.append(trade_entry)
   os.makedirs(f"../assets/json/transactions", exist_ok=True)
   with open(f"../assets/json/transactions/trades_{league.year}.json", 'w') as f:
       json.dump(all_trades, f, indent=1)
       
def generate_trade_network_json(league, trades):
    teams = league.teams
   # Calculate trade relationships
    colors = [f'hsl({h}, 70%, 50%)' for h in np.linspace(0, 360, len(teams))]
    nodes = [{"id": clean_team_name(team.team_name), "name": clean_team_name(team.team_name), "itemStyle": {"color": color}} 
                for team, color in zip(teams, colors)]
    
    edge_dict = {}
    for trade in trades:
        team_list = list(set([t.team_name for t, action, p, _ in trade.actions if action == 'TRADED']))
        if len(team_list) == 2:
            trade_details = {team_list[0]: [], team_list[1]: []}
            for team, action, player_, _ in trade.actions:
                if action == 'TRADED':
                    trade_details[team.team_name].append(player_.name)
                    
            key = tuple(sorted([team_list[0], team_list[1]]))
            tooltip = f"{key[0]}: {', '.join(trade_details[key[0]])} ⟷ {key[1]}: {', '.join(trade_details[key[1]])}"
            
            if key in edge_dict:
                edge_dict[key]["value"] += 1
            else:
                edge_dict[key] = {
                    "source": key[0],
                    "target": key[1],
                    "value": 1,
                    "tooltip": {"show": True},
                    "name": tooltip
                }

    echarts_data = {
        "title": {"text": "Trade Network", "left": "center", "top": "5%", "textStyle": {"fontSize": 20}, "show": False},
        "series": [{
            "type": "graph",
            "layout": "circular", 
            "symbolSize": 50,
            "roam": True,
            "label": {"show": True},
            "edgeSymbol": ["circle", "arrow"],
            "edgeSymbolSize": [4, 10],
            "data": nodes,
            "links": list(edge_dict.values()),
            "lineStyle": {"opacity": 0.9, "width": 2, "curveness": 0}
        }],
        "grid": {"top": "15%"}
    }

    os.makedirs(f"../assets/json/transactions", exist_ok=True)
    with open(f"../assets/json/transactions/network_trades_{league.year}.json", 'w') as f:
       json.dump(echarts_data, f, indent=2)
       
def create_position_contribution_chart(team, week=None, through_week=None, box_scores=None):
    """Creates single position contribution pie chart, either for one week or averaged through a week"""
    pos_points = {'QB': 0, 'RB': 0, 'WR': 0, 'TE': 0, 'D/ST': 0, 'K': 0}
   
    def _get_week_points(w):
        box = next((b for b in box_scores[w] if b.home_team == team or b.away_team == team), None)
        if box:
            lineup = box.home_lineup if box.home_team == team else box.away_lineup
            week_points = {'QB': 0, 'RB': 0, 'WR': 0, 'TE': 0, 'D/ST': 0, 'K': 0}
            starters = [p for p in lineup if p.slot_position != 'BE' and p.slot_position != 'IR']
            for player in starters:
                if player.position in week_points:
                    week_points[player.position] += player.points
            return week_points
        return None

    if week:
        pos_points = _get_week_points(week)
    elif through_week:
        week_points = [_get_week_points(w) for w in range(1, through_week + 1)]
        week_points = [w for w in week_points if w]  # Remove None values
        for pos in pos_points:
            pos_points[pos] = sum(w[pos] for w in week_points) / len(week_points)

    chart = {
        "tooltip": {
            "trigger": "item",
            "formatter": "{a} <br/>{b}: {d}%" 
        },
        "legend": {
            "orient": "vertical",
            "left": "left",
            "data": list(pos_points.keys())
        },
        "series": [{
            "name": "Position Points",
            "type": "pie", 
            "radius": ["50%", "70%"],
            "avoidLabelOverlap": False,
            "data": [
                {"value": round(points,1), "name": pos}
                for pos, points in pos_points.items() if points > 0
            ]
        }]
    }
    os.makedirs(f"../assets/json/team_data", exist_ok=True)
    if week:
        with open(f"../assets/json/team_data/{team.team_abbrev}_2024_Week_{week}_pie.json", 'w') as f:
            json.dump(chart, f, indent=2)
    else:
        with open(f"../assets/json/team_data/{team.team_abbrev}_2024_pie.json", 'w') as f:
            json.dump(chart, f, indent=2)
           
def create_playoff_bracket_mermaid(league: League) -> str:
    """Creates a Mermaid diagram showing playoff bracket.
    Automatically determines playoff teams and seeding from league data.
    """
    # Get playoff settings
    num_playoff_teams = league.settings.playoff_team_count
    
    # Get teams and sort by playoff seeding
    teams = league.teams
    playoff_teams = sorted(teams, 
                         key=lambda x: x.final_standing if x.final_standing != 0 else x.standing,
                         reverse=False)[:num_playoff_teams]
    
    # Start mermaid graph
    mermaid = ["graph LR"]
    
    # Create nodes for playoff teams
    for i, team in enumerate(playoff_teams):
        seed = i + 1
        node_id = f"T{seed}"
        mermaid.append(f'    {node_id}["{seed}. {clean_team_name(team.team_name)}"]')
        
    # Create bracket structure
    first_round = num_playoff_teams // 2
    for i in range(first_round):
        top_seed = i * 2 + 1
        bottom_seed = i * 2 + 2
        match_id = f"M{i+1}"
        winner_to = f"W{i+1}"
        
        # Add matchup node
        mermaid.append(f'    {match_id}(("vs"))')
        
        # Connect teams to matchup
        mermaid.append(f'    T{top_seed} --> {match_id}')
        mermaid.append(f'    T{bottom_seed} --> {match_id}')
        
        # Add winner node and connection for first round
        if i < first_round // 2:
            mermaid.append(f'    {winner_to}[/"Winner"/]') 
            mermaid.append(f'    {match_id} --> {winner_to}')
            
            # Connect winners to championship if applicable
            if first_round == 2:
                champ_id = "CHAMP"  
                mermaid.append(f'    {champ_id}(("vs"))')
                mermaid.append(f'    W1 --> {champ_id}')
                mermaid.append(f'    W2 --> {champ_id}')
                mermaid.append(f'    WINNER[/"Champion"/]')
                mermaid.append(f'    {champ_id} --> WINNER')

    # Add style
    mermaid.append("    classDef default fill:#fff,stroke:#333,stroke-width:2px;")
    mermaid.append("    classDef matchup fill:#f9f9f9,stroke:#666;")
    
    return "\n".join(mermaid)

def generate_trade_analyzer_data(league, week):
    """Generate player data for trade analyzer"""
    os.makedirs("../assets/json/trade_analyzer", exist_ok=True)
    
    player_data = []
    for team in league.teams:
        for player in team.roster:
            if player.injuryStatus != 'INJURY_RESERVE':
                # Calculate remaining weeks
                remaining_weeks = 17 - week
                ros_projection = (player.projected_total_points / 17) * remaining_weeks
                
                # Get average points from actual games played
                scores = [player.stats.get(w, {}).get('points', 0) 
                        for w in range(1, week + 1)]
                avg_points = player.avg_points
                
                player_data.append({
                    "id": player.playerId,
                    "name": player.name,
                    "position": player.position,
                    "team": clean_team_name(team.team_name),
                    "total_points": round(player.total_points, 2),
                    "avg_points": round(avg_points, 2),
                    "ros_projection": round(ros_projection, 2)
                })

    with open(f"../assets/json/trade_analyzer/players_{league.year}.json", "w") as f:
        json.dump(player_data, f, indent=2)
        
def generate_matchup_data_json(league, week, box_scores, news_data):
    """Generate JSON data for next week's matchups"""
    matchups = league.box_scores(week+1)  # Get next week's matchups
    matchup_data = []
    
    for matchup in matchups:
        if not matchup.away_team:  # Skip bye weeks
            continue
            
        home_team = matchup.home_team
        away_team = matchup.away_team
        
        # Get historical h2h records
        h2h_wins = 0
        total_games = 0
        avg_home_score = 0
        avg_away_score = 0
        
        for h_week, (opponent, score) in enumerate(zip(home_team.schedule[:week], home_team.scores[:week])):
            if opponent.team_id == away_team.team_id:
                total_games += 1
                if score > opponent.scores[h_week]:
                    h2h_wins += 1
                avg_home_score += score
                avg_away_score += opponent.scores[h_week]
                
        avg_home_score = avg_home_score/total_games if total_games > 0 else 0
        avg_away_score = avg_away_score/total_games if total_games > 0 else 0
        
        # Get position strength rankings
        home_pos_stats = get_positional_scoring_amounts(box_scores, week, home_team)
        away_pos_stats = get_positional_scoring_amounts(box_scores, week, away_team)
        
        # Get injuries
        home_injuries = []
        away_injuries = []
        if news_data:
            for team_news in news_data.get('injuries', []):
                for news in team_news.get('injuries', []):
                    player_name = news.get('athlete', {}).get('displayName', '').lower()
                    if any(player_name == p.name.lower() for p in home_team.roster):
                        home_injuries.append({
                            'player': news.get('athlete', {}).get('displayName', ''),
                            'status': news.get('status', ''),
                            'description': news.get('longComment', '')
                        })
                    elif any(player_name == p.name.lower() for p in away_team.roster):
                        away_injuries.append({
                            'player': news.get('athlete', {}).get('displayName', ''),
                            'status': news.get('status', ''),
                            'description': news.get('longComment', '')
                        })
        
        matchup_data.append({
            'home_team': clean_team_name(home_team.team_name),
            'away_team': clean_team_name(away_team.team_name),
            'home_projection': matchup.home_projected,
            'away_projection': matchup.away_projected,
            'h2h_record': f"{h2h_wins}-{total_games-h2h_wins}",
            'avg_score': f"{avg_home_score:.1f}-{avg_away_score:.1f}",
            'home_injuries': home_injuries,
            'away_injuries': away_injuries,
            'position_comparison': {
                pos: {
                    'home': round(sum(home_pos_stats.get(pos, [0]))/len(home_pos_stats.get(pos, [1])), 1),
                    'away': round(sum(away_pos_stats.get(pos, [0]))/len(away_pos_stats.get(pos, [1])), 1)
                }
                for pos in get_non_flex_positions(box_scores, 1)
            }
        })
    
    os.makedirs("../assets/json/matchups", exist_ok=True)
    with open(f"../assets/json/matchups/week_{week+1}.json", 'w') as f:
        json.dump(matchup_data, f, indent=2)