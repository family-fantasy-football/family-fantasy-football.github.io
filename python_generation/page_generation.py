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

def generate_about_md(league, week, teams, box_scores):
    
    generate_roster_table(league, week-1)
    generate_standings_table(league, week-1)
    create_standings_bump_json(teams, week)
    for pos in get_non_flex_positions(box_scores, 1):
        create_weekly_position_rankings_json(teams,week, box_scores, pos)
    generate_echarts_heatmap_json(teams, box_scores, week)
    
    bump_chart_data_path = '../assets/json/bump_chart_data.json'
    qb_data_path = "../assets/json/weekly_qb_rankings.json"
    rb_data_path = "../assets/json/weekly_rb_rankings.json"
    te_data_path = "../assets/json/weekly_te_rankings.json"
    wr_data_path = "../assets/json/weekly_wr_rankings.json"
    avg_pos_data_path = "../assets/json/heatmap_config.json"
    # Load JSON data from file
    with open(bump_chart_data_path, "r") as json_file:
        bump_chart_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_bump_chart_json = json.loads(bump_chart_data)
    formatted_bump_chart_json = json.dumps(parsed_bump_chart_json, indent=4)  # Prettify JSON

    with open(qb_data_path, "r") as json_file:
        qb_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_qb_json = json.loads(qb_data)
    formatted_qb_json = json.dumps(parsed_qb_json, indent=4)  # Prettify JSON
    
    with open(rb_data_path, "r") as json_file:
        rb_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_rb_json = json.loads(rb_data)
    formatted_rb_json = json.dumps(parsed_rb_json, indent=4)  # Prettify JSON
    
    with open(wr_data_path, "r") as json_file:
        wr_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_wr_json = json.loads(wr_data)
    formatted_wr_json = json.dumps(parsed_wr_json, indent=4)  # Prettify JSON
    
    with open(te_data_path, "r") as json_file:
        te_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_te_json = json.loads(te_data)
    formatted_te_json = json.dumps(parsed_te_json, indent=4)  # Prettify JSON
    
    with open(avg_pos_data_path, "r") as json_file:
        avg_pos_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_avg_pos_json = json.loads(avg_pos_data)
    formatted_avg_pos_json = json.dumps(parsed_avg_pos_json, indent=4)  # Prettify JSON
    
    
    top_scorer = max(teams, key=lambda x: x.points_for)
    least_scorer = min(teams, key=lambda x: x.points_for)
    top_scorer_name = get_manager_names(top_scorer.owners)
    least_scorer_name = get_manager_names(least_scorer.owners)
    
    highest_week = get_highest_scoring_week(week, box_scores)
    lowest_week = get_lowest_scoring_week(week, box_scores)

    luckiest_team = 0
    unluckiest_team = 0
    luckiest_factor = 0
    unluckiest_factor = 0
    for team in teams:
        outcomes = team.outcomes[:week]
        scores = team.scores[:week]
        schedule = team.schedule[:week]
        mov = team.mov[:week]
        expected_wins, actual_wins, luck_factor, close_wins, close_losses = get_luck_values(team, outcomes, mov, teams, week)
        if luck_factor > luckiest_factor:
            luckiest_team = team
            luckiest_factor = luck_factor
        if luck_factor < unluckiest_factor:
            unluckiest_team = team
            unluckiest_factor = luck_factor
    
    
    # Define the Markdown content
    content = f"""\
---
layout: page
title: home
permalink: /
# subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Motto. Etc.

profile:
  align: center
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info:

news: true # includes a list of news items
selected_papers: false
social: false # includes social icons at the bottom of the page
pretty_table: True
chart:
  echarts: true
---

## Welcome to the site for the Family Fantasy Footbal League! We are currently in the 2024-25 season. This site t is clearly still under development

<div style="margin-bottom: 30px;">

</div>


The current top scorer is: {top_scorer_name} ({top_scorer.points_for:.2f})

The current top scorer is: {least_scorer_name} ({least_scorer.points_for:.2f})

Highest Scoring Week: {get_manager_names(highest_week[0].owners)} - {highest_week[2]:.2f} points (Week {highest_week[1]})

Lowest Scoring Week: {get_manager_names(lowest_week[0].owners)} - {lowest_week[2]:.2f} points (Week {lowest_week[1]})

Luckiest Team: {get_manager_names(luckiest_team.owners)} ({luckiest_factor:.1f}) Wins Above Expected

Unluckiest Team: {get_manager_names(unluckiest_team.owners)} ({unluckiest_factor:.1f}) Wins Below Expected


### Current Standings:

<table
    data-click-to-select="true"
    data-height="690"
    data-pagination="true"
    data-search="false"
    data-toggle="table"
    data-url="{{{{ "/assets/json/standings.json"}}}}">
    <thead>
        <tr>
            <th data-field="team" data-halign="left" data-align="left" data-sortable="true">Team What</th>
            <th data-field="record" 
                data-halign="center" 
                data-align="center" 
                data-sortable="true"
                data-sort-name="record_sort">Record</th>
            <th data-field="record_sort" data-sortable="true" data-visible="false">Record Sort</th>
            <th data-field="last3" data-halign="center" data-align="center" data-sortable="true">Last 3 Games</th>
        </tr>
    </thead>
</table>

<br><br>
<br><br>


```echarts
{formatted_bump_chart_json}
```
<br><br>
<br><br>

### Average Position Rankings
```echarts
{formatted_avg_pos_json}
````


### Position Breakdowns By Week
<br><br>

##### QB
```echarts
{formatted_qb_json}
```

##### RB
```echarts
{formatted_rb_json}
```

##### WR
```echarts
{formatted_wr_json}
```

##### TE
```echarts
{formatted_te_json}
```
"""
    # Write the content to 'about.md'
    with open("../_pages/about.md", "w") as file:
        file.write(content)



def generate_indv_team_page_md(league, week, team):
    
    content = f"""\
---
layout: page
title: {team.team_name}
description:
img: assets/img/{team.team_abbrev}_{league.year}.jpg
importance: {team.team_id+1}
category: {league.year}-{league.year-1999}
related_publications: false
chart:
  echarts: true
pretty_table: True
---

### <center> Through Week {week} </center>

<table
 data-click-to-select="true"
 data-height="1100"
 data-search="false"
 data-toggle="table"
 data-url="{{{{ "/assets/json/team_rosters/{team.team_abbrev}_{league.year}.json"}}}}">
 <thead>
   <tr>
     <th data-field="player_name" data-halign="left" data-align="left" data-sortable="true">Player</th>
     <th data-field="pos" data-halign="center" data-align="center" data-sortable="true">Position</th>
     <th data-field="total_points" data-halign="center" data-align="center" data-sortable="true">Total Points</th>
     <th data-field="proj_points" data-halign="center" data-align="center" data-sortable="true">Projected Points</th>
     <th data-field="avg_points" data-halign="center" data-align="center" data-sortable="true">Avg. Points</th>
     <th data-field="pct_perform" data-halign="center" data-align="center" data-sortable="true">Performance</th>
   </tr>
 </thead>
</table>
"""

    # Write the content to 'about.md'
    with open(f"../_projects/{team.team_abbrev}_{league.year}.md", "w") as file:
        file.write(content)