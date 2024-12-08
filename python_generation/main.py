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

from utils import *
from fetch import *
from make_assests import *
from page_generation import *

def main():
    SWID = "{42614A28-F6F5-4052-A14A-28F6F52052AF}" 
    ESPN_S2 = "AECeHAkR7FZuTvVWSEnMRIA29wVeroZhvd7fHHy5tZvIUdIp4XIZaglA17V6g2rulDDFMCUiC%2BpeXNqWzEJTpjTJsz5Zv2DTMOIjeX0JrC6CYs8kDidYeF0HHkI78OG2O%2Bs6f%2FUPVSwXRBZEGMKPDdKl%2BE0a7na225JN4bC80tD9RXFv32kqqtEk%2Bgw1hgQ968ARiAdt69axAvjryW57rj58sYK4oMJPxjtPbh9tATi%2BSI2AmQ0dNPXZfRTA%2FFgCtgzyxWNwbKT2boYeDfFe7rm8idW47lnavsfYGwWjVpddVY6%2BcupF7uoc9AeVFQ5xNUY%3D"
    LEAGUE_ID = 697625923
    YEAR = 2024
    league=  League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
    week = league.nfl_week
    teams = league.teams
    weekly_rankings = []
    reg_season_length= league.settings.reg_season_count
    box_scores_cache = {}  # Initialize cache
    teams = sorted(league.teams, key=lambda x: (x.wins, x.points_for), reverse=True)
    def get_box_scores(week, cache=box_scores_cache):
        if week not in cache:
            cache[week] = league.box_scores(week)
        return cache[week]
    box_scores = {week: get_box_scores(week) for week in range(1, reg_season_length + 1)}
    
    save_team_logos(league)
    generate_roster_table(league, week-1)
    generate_standings_table(league, week-1)
    
    generate_about_md(league, reg_season_length, teams, box_scores)
    for team in teams:
        generate_indv_team_page_md(league, league.nfl_week, team)
    
if __name__ == "__main__":
    main()
