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
import matplotlib.pyplot as plt
import json
import requests
from datetime import datetime, timedelta



from utils import *
from fetch import *
from make_assests import *
from page_generation import *

def main():
    SWID = "{42614A28-F6F5-4052-A14A-28F6F52052AF}" 
    ESPN_S2 = "AECeHAkR7FZuTvVWSEnMRIA29wVeroZhvd7fHHy5tZvIUdIp4XIZaglA17V6g2rulDDFMCUiC%2BpeXNqWzEJTpjTJsz5Zv2DTMOIjeX0JrC6CYs8kDidYeF0HHkI78OG2O%2Bs6f%2FUPVSwXRBZEGMKPDdKl%2BE0a7na225JN4bC80tD9RXFv32kqqtEk%2Bgw1hgQ968ARiAdt69axAvjryW57rj58sYK4oMJPxjtPbh9tATi%2BSI2AmQ0dNPXZfRTA%2FFgCtgzyxWNwbKT2boYeDfFe7rm8idW47lnavsfYGwWjVpddVY6%2BcupF7uoc9AeVFQ5xNUY%3D"
    LEAGUE_ID = 697625923
    YEAR = 2025
    league=  League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
    week = league.nfl_week
    teams = league.teams
    weekly_rankings = []
    week = 1
    reg_season_length= week
    box_scores_cache = {}  # Initialize cache
    teams = sorted(league.teams, key=lambda x: (x.wins, x.points_for), reverse=True)
    def get_box_scores(week, cache=box_scores_cache):
        if week not in cache:
            cache[week] = league.box_scores(week)
        return cache[week]
    box_scores = {week: get_box_scores(week) for week in range(1, week + 1)}
    activity_size = 350  # Increased size to minimize API calls
    transactions = league.recent_activity(size=activity_size)
    waiver_adds = []
    fa_adds = []
    trades = []
    response = requests.get('https://site.api.espn.com/apis/site/v2/sports/football/nfl/injuries')
    news_data = response.json()
    for activity in transactions:
        activity_str = str(activity)
        if "WAIVER" in activity_str:
            waiver_adds.append(activity)
        elif "FA ADDED" in activity_str:
            fa_adds.append(activity)
        if "TRADED" in activity_str:
            trades.append(activity)
    generate_team_json(league, teams, box_scores, week, trades, transactions)
    generate_weekly_scores_json(teams, week, league)
    save_team_logos(league)
    generate_roster_table(league, week)
    generate_standings_table(league, week)
    news_data = []
    generate_about_md(league, week, teams, box_scores)
    for team in teams:
        generate_indv_team_page_md(league, week, team, box_scores)
        generate_team_weekly_recap(league, team.team_name,box_scores, news_data, week)
        
    combine_draft_json()
    # # week = 14
    generate_league_weekly_recap_markdown(league, box_scores, week)
    
    generate_draft_page()
    generate_players_page(league, week)
    create_records_json(league, box_scores, week)
    create_team_history_json(league)
    generate_history_page()
    generate_records_page()
    generate_trades_page(league, trades)
    generate_waivers_page(league, waiver_adds, fa_adds, trades)
    # generate_playoff_page(league, week)
    
    generate_trade_analyzer_data(league, week)
    generate_trade_analyzer_page()
    
    generate_matchups_preview(league, week, box_scores, news_data)
    generate_player_comparison_data(league, week)
    
    # archive_team_pages(league, week, teams, box_scores)
    # generate_archive_index()
    
    generate_payment_page(league, teams)

    
    
if __name__ == "__main__":
    main()
