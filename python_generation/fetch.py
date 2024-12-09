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
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import os
import json

from utils import *

def save_team_logos(league):
    os.makedirs('../assets/img', exist_ok=True)
    
    options = Options()
    # options = webdriver.ChromeOptions()
    # options.binary_location = '/usr/bin/chromium-browser'  # Path to the Chromium binary
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    options.add_argument('--no-sandbox')  # Disable the sandbox for Chromium in Docker
    options.add_argument('--disable-dev-shm-usage')  # Useful for Docker environments

    # Initialize the webdriver with Chromium
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com')

    for team in league.teams:
        if team.logo_url:
            driver.get(team.logo_url)
            driver.save_screenshot(f"../assets/img/{clean_team_name(team.team_abbrev)}_{league.year}.jpg")
            
    driver.quit()

def clean_team_name(team_name):
    return team_name.encode('ascii', 'ignore').decode('ascii')

def get_manager_names(owners: list) -> str:
    """Convert owners list to formatted string of full names"""
    manager_names = []
    for owner in owners:
        first_name = owner.get('firstName', '')
        last_name = owner.get('lastName', '')
        if first_name and last_name:
            manager_names.append(f"{first_name} {last_name}")
        else:
            manager_names.append(owner.get('displayName', 'Unknown Manager'))
    
    if len(manager_names) > 1:
        return f"{', '.join(manager_names[:-1])} and {manager_names[-1]}"
    elif manager_names:
        return manager_names[0]
    return "Unknown Manager"

def calculate_scoring_volatility(league, scores: List[float]) -> float:
    """Calculate standard deviation of scores"""
    return round(statistics.stdev(scores)/np.sqrt(league.settings.reg_season_count), 2) if len(scores) > 1 else 0


def week_of_transaction(epoch):
    week_2_start = datetime(2024, 9, 10, 3, 0, 0, tzinfo=ZoneInfo("America/New_York")).timestamp()  
    week_occured = math.floor((epoch/1000 - week_2_start)/60/60/24/7 + 2)
    return week_occured

def calculate_expected_wins(teams, through_week):
    expected_wins = {team.team_id: 0 for team in teams}
    num_teams = len(teams)
    
    for week in range(1, through_week + 1):
        # Get all scores for the week
        week_scores = []
        for team in teams:
            if week < len(team.scores):
                week_scores.append((team.team_id, team.scores[week]))
        
        # Sort by score high to low
        week_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Assign points based on teams outscored
        for i, (team_id, _) in enumerate(week_scores):
            teams_outscored = num_teams - 1 - i  # -1 because you can't outscore yourself
            expected_wins[team_id] += teams_outscored / (num_teams - 1)
    
    return expected_wins

  
def get_expected_points(league, player_id, through_week):
    return league.player_info(playerId = player_id).stats[0]['projected_points']/17*through_week

def grade_pick(value_diff, mean_value_diff, std_value_diff):
    """Grade a pick based on how the value_diff compares to league's mean and std deviation."""
    z_score = (value_diff - mean_value_diff) / std_value_diff  # Calculate z-score

    # Assign grades based on z-score
    if z_score >= 1.:
        return "A"  # Significantly better than average
    elif z_score >= 0.:
        return "B"  # Slightly above average
    elif z_score >= -.75:
        return "C"  # Around average
    else:
        return "D"  # Below average

def get_highest_scoring_week(through_week, box_scores):
        highest_week = None
        highest_score = 0
        
        for week in range(1, through_week + 1):
            scores = box_scores[week]
            for score in scores:
                if score.home_score > highest_score:
                    highest_score = score.home_score
                    highest_week = (score.home_team, week, score.home_score)
                if score.away_score > highest_score:
                    highest_score = score.away_score
                    highest_week = (score.away_team, week, score.away_score)
        return highest_week
    
def get_lowest_scoring_week(through_week, box_scores):
        lowest_week = None
        lowest_score = 1000
        
        for week in range(1, through_week + 1):
            scores = box_scores[week]
            for score in scores:
                if score.home_score < lowest_score:
                    lowest_score = score.home_score
                    lowest_week = (score.home_team, week, score.home_score)
                if score.away_score < lowest_score:
                    lowest_score = score.away_score
                    lowest_week = (score.away_team, week, score.away_score)
        return lowest_week

def get_margins_of_victory_records(through_week, box_scores):
    highest_margin = (0, None, None, None, None, None)
    lowest_margin = (float('inf'), None, None, None, None, None)
    
    for week in range(1, through_week + 1):
        scores = box_scores[week]
        for score in scores:
            margin = abs(score.home_score - score.away_score)
            if score.home_score > score.away_score:
                winner = score.home_team
                loser = score.away_team
                win_score = score.home_score
                lose_score = score.away_score
            else:
                winner = score.away_team
                loser = score.home_team
                win_score = score.away_score
                lose_score = score.home_score
            
            if margin > highest_margin[0]:
                highest_margin = (margin, week, winner, loser, win_score, lose_score)
            if 0 < margin < lowest_margin[0]:
                lowest_margin = (margin, week, winner, loser, win_score, lose_score)
                
    return highest_margin, lowest_margin

def get_best_trades(trades):
    trade_impacts = []
    for trade in trades:
        trade_epoch = trade.date
        trade_week = week_of_transaction(trade_epoch)
        
        # Get teams involved in trade using your existing method
        team_list = list(set([t for t, action, p, _ in trade.actions if action == 'TRADED']))
        
        # Group players by team they're leaving
        team_trades = {team.team_id: {'leaving': [], 'receiving': []} for team in team_list}
        
        for team, action, player, _ in trade.actions:
            if action == 'TRADED':
                new_team = next(item for item in team_list if item != team)
                team_trades[team.team_id]['leaving'].append(player)
                team_trades[new_team.team_id]['receiving'].append(player)
        
        # Calculate impact for each team
        for team_id, players in team_trades.items():
            team = next(t for t in team_list if t.team_id == team_id)
            
            # Calculate performance for players leaving
            leaving_before = []
            leaving_after = []
            for player in players['leaving']:
                active_weeks = [
                    week for week in player.stats.keys()
                    if week != 0 and
                    isinstance(player.stats[week], dict) and
                    player.stats[week]['points'] > 0
                ]
                active_weeks.sort()
                
                if active_weeks:
                    before_weeks = [w for w in active_weeks if w < trade_week][-3:]
                    after_weeks = [w for w in active_weeks if w >= trade_week]
                    
                    if before_weeks:
                        leaving_before.extend([player.stats[w]['points'] for w in before_weeks])
                    if after_weeks:
                        leaving_after.extend([player.stats[w]['points'] for w in after_weeks])
            
            # Calculate performance for players receiving
            receiving_before = []
            receiving_after = []
            for player in players['receiving']:
                active_weeks = [
                    week for week in player.stats.keys()
                    if week != 0 and
                    isinstance(player.stats[week], dict) and
                    player.stats[week]['points'] > 0
                ]
                active_weeks.sort()
                
                if active_weeks:
                    before_weeks = [w for w in active_weeks if w < trade_week][-3:]
                    after_weeks = [w for w in active_weeks if w >= trade_week]
                    
                    if before_weeks:
                        receiving_before.extend([player.stats[w]['points'] for w in before_weeks])
                    if after_weeks:
                        receiving_after.extend([player.stats[w]['points'] for w in after_weeks])
            
            # Calculate averages
            leaving_before_avg = sum(leaving_before) / len(leaving_before) if leaving_before else 0
            leaving_after_avg = sum(leaving_after) / len(leaving_after) if leaving_after else 0
            receiving_before_avg = sum(receiving_before) / len(receiving_before) if receiving_before else 0
            receiving_after_avg = sum(receiving_after) / len(receiving_after) if receiving_after else 0
            
            # Calculate net impact (difference in improvement between received and lost players)
            trade_impact = (receiving_after_avg - receiving_before_avg) - (leaving_after_avg - leaving_before_avg)
            
            if (leaving_before or receiving_before) and (leaving_after or receiving_after):
                trade_impacts.append({
                    'week': trade_week,
                    'team': clean_team_name(team.team_name),
                    'team_abbrev': team.team_abbrev,
                    'managers': get_manager_names(team.owners),
                    'gave_up': [p.name for p in players['leaving']],
                    'gave_up_formatted': [format_name(p.name) for p in players['leaving']],
                    'received': [p.name for p in players['receiving']],
                    'received_formatted': [format_name(p.name) for p in players['receiving']],
                    'leaving_before_avg': leaving_before_avg,
                    'leaving_after_avg': leaving_after_avg,
                    'receiving_before_avg': receiving_before_avg,
                    'receiving_after_avg': receiving_after_avg,
                    'improvement': trade_impact,
                    'num_before': len(set(before_weeks)) if 'before_weeks' in locals() else 0,
                    'num_after': len(set(after_weeks)) if 'after_weeks' in locals() else 0
                })
            trade_impacts.sort(key=lambda x: x['improvement'], reverse=True)
            
            
    return trade_impacts

def get_best_acquisitions(league, waiver_adds, fa_adds, trades):
    pickups = {}
    # print("\nProcessing Pickups:")
    for activity in (waiver_adds + fa_adds):
        for team, action, player_, bid in activity.actions:
            if action in ['WAIVER ADDED', 'FA ADDED']:
                player = league.player_info(playerId=player_.playerId)
                # print(f"\nChecking {player.name} added by {team.team_name}")
                # Get all weeks player scored points
                # Get all activity for this player to track ownership
                
                # Get next transaction for this player
                next_move = None
                for act in (waiver_adds + fa_adds + trades):
                    if act.date > activity.date:  # Only look at later transactions
                        for t, a, p, _ in act.actions:
                            if p.playerId == player.playerId:
                                next_move = act
                                break
                        if next_move:
                            break
                
                # Skip if player was dropped/traded within a week
                if next_move and (next_move.date - activity.date) < 3*7 * 24 * 60 * 60 * 1000:  # 7 days in milliseconds
                    continue
                
                # Create unique key for this pickup
                pickup_key = (player.playerId, team.team_id, week_of_transaction(activity.date))
                
                # Skip if we've already processed this pickup
                if pickup_key in pickups:
                    continue
                
                
                player_moves = []
                for act in (waiver_adds + fa_adds + trades):
                    for t, a, p, _ in act.actions:
                        if p.playerId == player.playerId:
                            player_moves.append((week_of_transaction(act.date), a, t))
                player_moves.sort(key=lambda x: x[0])
                
                
                active_weeks = [
                    week for week in player.stats.keys() 
                    if week != 0  and len(player.stats[week]['breakdown']) > 3 ]
                active_weeks.sort()
                # print(f"Active weeks found: {active_weeks}")
                acq_epoch = activity.date
                acq_week = week_of_transaction(acq_epoch)
                if active_weeks:
                    end_week = None
                    for move_week, move_action, move_team in player_moves:
                        if move_week > acq_week and (
                            move_action == ('TRADED' or 'DROPPED')):
                            # (move_action in ['WAIVER ADDED', 'FA ADDED'] and move_team != team)):
                            end_week = move_week
                            break
                        # Get all weeks after pickup
                        after_weeks = [
                            week for week in active_weeks
                            if week >= acq_week and player.stats[week]['points'] > 0 and abs(week - acq_week) >=1 
                        ]
                        # print(f"After weeks found: {after_weeks}")
                        
                        before_weeks = [
                            week for week in active_weeks
                            if week < acq_week and player.stats[week]['points'] > 0 and abs(week - acq_week) >=2
                        ][-3:]
                        # print(f"Before weeks found: {before_weeks}")
                        
                        # Calculate averages
                        before_avg = (sum(player.stats[week]['points'] for week in before_weeks) / len(before_weeks)) if before_weeks else 0
                        after_avg = sum(player.stats[week]['points'] for week in after_weeks) / len(after_weeks) if after_weeks else 0
                        
                        if len(after_weeks)>2 and (after_avg > 0 or before_avg > 0) and len(before_weeks) > 2:
                            # print(f"Before avg: {before_avg:.2f}, After avg: {after_avg:.2f}")
                            pickups[pickup_key] = {
                                'week': acq_week,
                                'player_name': player.name,
                                'position': player.position,
                                'team': clean_team_name(team.team_name),
                                'prev_avg': before_avg,
                                'new_avg': after_avg,
                                'improvement': after_avg - before_avg,
                                'num_weeks_before': len(before_weeks),
                                'num_weeks_after': len(after_weeks)
                            }

    return list(pickups.values())

def get_benchings(through_week, box_scores_dict, teams):
    worst_benchings = {}  # Use dict to track unique player-week combinations
    for week in range(1, through_week + 1):
        for team in teams:
            box_scores = box_scores_dict[week]
            box = next((b for b in box_scores if b.home_team == team or b.away_team == team), None)
            if box:
                lineup = box.home_lineup if box.home_team == team else box.away_lineup
                starters = [p for p in lineup if p.slot_position != 'BE' and p.slot_position != 'IR']
                bench = [p for p in lineup if p.slot_position == 'BE']
                
                # For each benched player
                for benched in bench:
                    max_points_lost = 0
                    worst_starter = None
                    position_lost = None
                    
                    # Check all eligible positions for this player
                    for slot in benched.eligibleSlots:
                        slot_starters = [s for s in starters if s.slot_position == slot]
                        if slot_starters:
                            worst_starter_at_pos = min(slot_starters, key=lambda x: x.points)
                            points_lost = benched.points - worst_starter_at_pos.points
                            if points_lost > max_points_lost:
                                max_points_lost = points_lost
                                worst_starter = worst_starter_at_pos
                                position_lost = slot
                    
                    if max_points_lost > 0:
                        # Use week-player combo as key to avoid duplicates
                        bench_key = (week, benched.name)
                        if bench_key not in worst_benchings or max_points_lost > worst_benchings[bench_key]['points_lost']:
                            worst_benchings[bench_key] = {
                                'week': week,
                                'team_name': clean_team_name(team.team_name),
                                'team_managers': team.owners,
                                'benched_player': benched.name,
                                'benched_points': benched.points,
                                'starter_player': worst_starter.name,
                                'starter_points': worst_starter.points,
                                'points_lost': max_points_lost,
                                'position': position_lost
                            }
    return worst_benchings

def get_streaks(outcomes):
    current_streak = 0
    streak_type = ''
    for outcome in reversed(outcomes):
        if not streak_type:
            streak_type = outcome
            current_streak = 1
        elif outcome == streak_type:
            current_streak += 1
        else:
            break
    
    longest_win_streak = 0
    longest_lose_streak = 0
    current_win_streak = 0
    current_lose_streak = 0
    
    for outcome in outcomes:
        if outcome == 'W':
            current_win_streak += 1
            current_lose_streak = 0
            longest_win_streak = max(longest_win_streak, current_win_streak)
        elif outcome == 'L':
            current_lose_streak += 1
            current_win_streak = 0
            longest_lose_streak = max(longest_lose_streak, current_lose_streak)
        else:  # Ties reset streaks
            current_win_streak = 0
            current_lose_streak = 0
    return longest_win_streak, longest_lose_streak, current_streak, streak_type

def get_efficiencies(through_week, box_scores_dict, team):
    weekly_effs = []
    total_bench_points = 0
    total_optimal_points = 0
    total_actual_points = 0
    priority_pos = ['QB', 'WR', 'RB', 'TE', 'RB/WR/TE' , 'OP']
    for week in range(1, through_week + 1):
        box_scores = box_scores_dict[week]
        box = next((b for b in box_scores if b.home_team == team or b.away_team == team), None)
        if box:
            lineup = box.home_lineup if box.home_team == team else box.away_lineup
            starters = [p for p in lineup if p.slot_position != 'BE' and p.slot_position != 'IR']
            bench = [p for p in lineup if p.slot_position == 'BE']
            
            # Calculate actual score
            actual_points = sum(p.points for p in starters)
            
            # Get position requirements from actual lineup
            pos_requirements = {}
            for player in starters:
                if player.slot_position in pos_requirements:
                    pos_requirements[player.slot_position] += 1
                else:
                    pos_requirements[player.slot_position] = 1
            
            # Calculate optimal score by position
            optimal_points = 0
            all_players = sorted(lineup, key=lambda x: x.points, reverse=True)
            used_players = set()
            pos_requirements = sort_dict_with_prioritized_keys(pos_requirements, priority_keys=priority_pos)
            # Fill each position with best available players
            for pos, count in pos_requirements.items() :
                # Get all players eligible for this position
                eligible = [p for p in all_players 
                            if pos in p.eligibleSlots 
                            and p.name not in used_players]
                
                # Take the top N players needed for this position
                for player in eligible[:count]:
                    optimal_points += player.points
                    used_players.add(player.name)
            
            if optimal_points > 0:
                efficiency = (actual_points / optimal_points) * 100
                weekly_effs.append(efficiency)
                bench_points =  optimal_points - actual_points
                total_bench_points += bench_points
                total_actual_points += actual_points
                total_optimal_points += optimal_points
                
    return weekly_effs, total_bench_points, total_optimal_points, total_actual_points

def get_positional_scoring_amounts(box_score_dict, through_week, team):
    positions = {'QB': [], 'RB': [], 'WR': [], 'TE': [], 'D/ST': [], 'K': []}
            
    for week in range(1, through_week + 1):
        box_scores = box_score_dict[week]
        box = next((b for b in box_scores if b.home_team == team or b.away_team == team), None)
        if box:
            lineup = box.home_lineup if box.home_team == team else box.away_lineup
            starters = [p for p in lineup if p.slot_position != 'BE' and p.slot_position != 'IR']
            for player in starters:
                if player.position in positions:
                    positions[player.position].append(player.points)
    return {pos: scores for pos, scores in positions.items() if scores}



def get_luck_values(team, outcomes, mov, teams, through_week):
    expected_wins_dict = calculate_expected_wins(teams, through_week)
    expected_wins = expected_wins_dict[team.team_id]
    actual_wins = outcomes.count('W')
    luck_factor = actual_wins - expected_wins
    
    close_games = sum(1 for margin in mov[:through_week] if margin is not None and abs(margin) < 5)
    close_wins = sum(1 for margin, outcome in zip(mov[:through_week], outcomes) 
                    if margin is not None and abs(margin) < 5 and outcome == 'W')
    close_losses = close_games - close_wins
    
    return expected_wins, actual_wins, luck_factor, close_wins, close_losses

def get_records_against(schedule, scores, outcomes):
    opponent_stats = {}
    for week, (opponent, score, outcome) in enumerate(zip(schedule, scores, outcomes)):
        if opponent.team_id not in opponent_stats:
            opponent_stats[opponent.team_id] = {
                'games': 0, 'wins': 0, 'points_for': 0, 'points_against': 0
            }
        
        opponent_stats[opponent.team_id]['games'] += 1
        opponent_stats[opponent.team_id]['points_for'] += score
        opponent_stats[opponent.team_id]['points_against'] += opponent.scores[week]
        if outcome == 'W':
            opponent_stats[opponent.team_id]['wins'] += 1
            
    return opponent_stats

def get_drafted_player_data(through_week, trades, league, transactions, draft_results):
    # Process trades to track players traded and their points after being traded
    traded_players = []
    for trade in trades:
        for team, action, player_, bid in trade.actions:
            # Get player info for the traded player
            player = league.player_info(playerId=player_.playerId)
            trade_epoch = trade.date
            trade_week = week_of_transaction(trade_epoch)  # Week the trade occurred
            
            # Calculate total points the player earned after the trade
            total_points_after_trade = 0
            for week in player.stats.keys():
                if week != 0 and week >= trade_week:  # Only consider points earned after the trade
                    total_points_after_trade += player.stats[week]['points']

            # Store player transaction info with points earned after the trade
            traded_players.append({
                "team": clean_team_name(team.team_name),
                "player_name": player.name,
                "trade_week": trade_week,
                "total_points_after_trade": total_points_after_trade,
                "trade_epoch": trade_epoch,
            })


    # Initialize a set to keep track of processed players and avoid considering multiple transactions
    processed_players = set()
    transactions = sorted(transactions, key=lambda activity: activity.date)
    # Process all transactions to calculate points earned before leaving the original team
    points_before_leave = []
    for activity in transactions:
        for team, action, player_, bid in activity.actions:
            # Skip this player if they've already been processed
            if player_.playerId in processed_players:
                continue
            
            player = league.player_info(playerId=player_.playerId)
            trans_epoch = activity.date
            trans_week = week_of_transaction(trans_epoch)  # Week the transaction occurred

            # Calculate total points the player earned before leaving the team
            total_points_before_leave = 0
            for week in player.stats.keys():
                if week != 0 and week < trans_week:  # Only consider points earned before the transaction
                    total_points_before_leave += player.stats[week]['points']

            # Store player transaction info with points earned before leaving the team
            points_before_leave.append({
                "team": clean_team_name(team.team_name),
                "player_name": player.name,
                "transaction_week": trans_week,
                "total_points_before_leave": total_points_before_leave,
                "transaction_epoch": trans_epoch,
            })
            
            # Mark the player as processed to ensure we only look at the first transaction
            processed_players.add(player_.playerId)

    # Combine transaction points with draft analysis
    all_players = []
    all_value_diffs = []

    # Create a mapping of player stats by player_id
    for team in league.teams:
        for player in team.roster:
            all_players.append({
                "player_id": player.playerId,
                "player_name": player.name,
                "total_points": player.total_points,  # Use the total points the player earned overall
                "team_id": team.team_id,  # The team that currently has the player
                "team_name": clean_team_name(team.team_name),
            })

    # Create a mapping of player stats for fast lookup
    player_stats = {player["player_id"]: player for player in all_players}

    # Merge draft data with player stats and trade info
    drafted_players = []
    for pick in draft_results:
        # Get stats for the drafted player
        player_stat = player_stats.get(pick.playerId, {})

        # Check if the player has a transaction week (either before leaving or after trade)
        player_transaction = next((p for p in points_before_leave if p['player_name'] == pick.playerName), None)
        player_trade = next((p for p in traded_players if p['player_name'] == pick.playerName), None)
        
        if player_transaction:
            # If the player has a transaction week, consider only the points before the transaction
            total_points_before_leave = player_transaction["total_points_before_leave"]
        else:
            total_points_before_leave = player_stat.get("total_points", 0)

        if player_trade:
            # If the player was traded, add points earned after the trade
            total_points_after_trade = player_trade["total_points_after_trade"]
        else:
            total_points_after_trade = 0

        # Calculate the total points for this pick (points before leaving + points after trade)
        total_points = total_points_before_leave + total_points_after_trade
        # Retrieve the expected points for the player
        expected_points = get_expected_points(league, pick.playerId, through_week)

        # Calculate value_diff for the player
        value_diff = total_points - expected_points  # Points earned - projected points
        
        # Add value_diff to list to compute league mean and std dev
        all_value_diffs.append(value_diff)
        
        
        drafted_players.append({
            "drafted_team_id": pick.team.team_id,
            'drafted_team': pick.team, # Store the team that drafted the player
            "player_id": pick.playerId,
            "player_name": pick.playerName,
            "round_num": pick.round_num,
            "round_pick": pick.round_pick,
            "draft_position": ((pick.round_num - 1) * league.settings.team_count) + pick.round_pick,
            "points_before_leave": total_points_before_leave,  # Include points before leaving
            "points_after_trade": total_points_after_trade,    # Include points after trade
            "total_points": total_points,
            "value_diff": value_diff,
        })
    return drafted_players, all_value_diffs

def get_draft_order(league):
    draft_order = {}
    for pick in league.draft:
        if pick.round_num == 1:  # Only look at first round picks
            draft_order[clean_team_name(pick.team.team_name)] = pick.round_pick
    return draft_order

def get_non_flex_positions(box_scores, week=1):
    # Look at first box score, first team's lineup
    first_box = box_scores[week][0]
    first_lineup = first_box.home_lineup
    
    # Get unique positions from starting slots (non-bench, non-IR)
    positions = set(player.position 
                   for player in first_lineup 
                   if player.slot_position != 'BE' 
                   and player.slot_position != 'IR'
                   and 'FLEX' not in player.slot_position)  # Exclude FLEX positions
    
    return sorted(list(positions))

def get_rostered_news(league: League) -> Dict:
        # Get all rostered players by name
        rostered_players = {}
        for team in league.teams:
            for player in team.roster:
                if player.lineupSlot != 'IR' or 'BE':
                    rostered_players[player.name.lower()] = {
                        'name': player.name,
                        'team_name': clean_team_name(team.team_name),
                        'position': player.position,
                        'team_abbrev': team.team_abbrev,
                        'lineup_slot': player.lineupSlot
                    }
        
        # Fetch from ESPN's main injury API
        response = requests.get('https://site.api.espn.com/apis/site/v2/sports/football/nfl/injuries')
        news_data = response.json()
        last_update_time = datetime.strptime(news_data['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
        last_update_time = last_update_time.replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        
        relevant_news = []
        for team in news_data.get('injuries', []):
            for news in team.get('injuries', []):
                player_name = news.get('athlete', {}).get('displayName', '').lower()
                if player_name in rostered_players:
                    if now-last_update_time <= timedelta(days=7):
                        relevant_news.append({
                            **rostered_players[player_name],
                            'status': news.get('status', 'Unknown'),
                            'description': news.get('longComment', ''),
                            'last_update': news.get('date')
                        })
        # Group the relevant news by team
        team_recaps = {}
        for news_item in relevant_news:
            team_name = news_item['team_name']
            if team_name not in team_recaps:
                team_recaps[team_name] = []
            team_recaps[team_name].append(news_item) 
            
        # Print the weekly recap for each team
        for team_name, news_items in team_recaps.items():
            print(f"Weekly Recap for {team_name}:")
            for news in news_items:
                print(f"  Player: {news['name']} ({news['position']})")
                print(f"    Status: {news['status']}")
                print(f"    Description: {news['description']}")
                print(f"    Last Update: {datetime.strptime(news['last_update'], '%Y-%m-%dT%H:%MZ')-timedelta(hours=5)} EST")
            print("-" * 50)  # Separator between teams
            
        return #sorted(relevant_news, key=lambda x: (x['team_name'],x['lineup_slot'], x['name']))
