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
                
            standings_data.append({
                'team': clean_team_name(team.team_name),
                'record': f"{team.wins}-{team.losses}",
                'last3': ''.join(recent_results)
            })
            
        return [
            {
                'id': i,
                'team': clean_team_name(team.team_name),
                'record': f"{team.wins}-{team.losses}",
                'last3': ''.join(team.outcomes[:through_week][-3:])
            }
            for i, team in enumerate(sorted(league.teams, key=lambda x: (x.wins, x.points_for), reverse=True))
        ]
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