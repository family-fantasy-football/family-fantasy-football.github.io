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
from datetime import datetime, timedelta
import glob

from utils import *
from fetch import *
from make_assests import *

def generate_about_md(league, week, teams, box_scores):
    create_weekly_scores_boxplot_json(teams, week)
    create_team_scatter_json(league, week)
    generate_roster_table(league, week)
    generate_standings_table(league, week)
    create_standings_bump_json(teams, week)
    for pos in get_non_flex_positions(box_scores, 1):
        create_weekly_position_rankings_json(teams,week, box_scores, pos)
    generate_echarts_heatmap_json(teams, box_scores, week)
    generate_analytics_json(league, teams, week, box_scores)
    opt_chart_data = f"../assets/json/analytics/optimization_chart.json"
    with open(opt_chart_data, "r") as json_file:
        opt_chart= json_file.read()
    # Ensure JSON is properly formatted
    parsed_opt_chart = json.loads(opt_chart)
    formatted_opt_chart = json.dumps(parsed_opt_chart, indent=4) 
    
    
    pos_chart_data = f"../assets/json/analytics/position_chart.json"
    with open(pos_chart_data, "r") as json_file:
        pos_chart= json_file.read()
    parsed_pos_chart = json.loads(pos_chart)
    formatted_pos_chart = json.dumps(parsed_pos_chart, indent=4) 
    bump_chart_data_path = '../assets/json/bump_chart_data.json'
    qb_data_path = "../assets/json/weekly_qb_rankings.json"
    rb_data_path = "../assets/json/weekly_rb_rankings.json"
    te_data_path = "../assets/json/weekly_te_rankings.json"
    wr_data_path = "../assets/json/weekly_wr_rankings.json"
    avg_pos_data_path = "../assets/json/heatmap_config.json"
    scatter_plot_data_path = "../assets/json/plots/scatter_data.json"
    boxplot_data_path = "../assets/json/plots/boxplot_data.json"
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
    
    with open(scatter_plot_data_path, "r") as json_file:
        scatter_plot_data = json_file.read()
    # Ensure JSON is properly formatted
    scatter_plot_json = json.loads(scatter_plot_data)
    formatted_scatter_plot_json = json.dumps(scatter_plot_json, indent=4)  # Prettify JSON
    
    with open(boxplot_data_path, "r") as json_file:
        boxplot_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_boxplot_plot_json = json.loads(boxplot_data)
    formatted_boxplot_plot_json = json.dumps(parsed_boxplot_plot_json, indent=4)
    
    
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
layout: about
title: home
permalink: /
# subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Motto. Etc.

profile:
  align: center
  image:
  image_circular: false # crops the image to make it circular
  more_info:

news: true # includes a list of news items
selected_papers: false
social: false # includes social icons at the bottom of the page
pretty_table: True
chart:
  echarts: true
---

## Welcome to the site for the Family Fantasy Footbal League! We are currently in the 2024-25 season.

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
    data-height="635"
    data-pagination="false"
    data-search="false"
    data-toggle="table"
    data-url="{{{{ "/assets/json/standings.json"}}}}">
    <thead>
        <tr>
            <th data-field="team" data-halign="left" data-align="left" data-sortable="true">Team</th>
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

```echarts
{formatted_scatter_plot_json}
```
<br><br>

```echarts
{formatted_boxplot_plot_json}
```
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

\n## Advanced Analytics\n
<br>
\n### Lineup Efficiency Over Time\n
```echarts
{formatted_opt_chart}
```\n
<br>
\n### Positional Advantages\n
```echarts
{formatted_pos_chart}
```\n
"""

    
    # Write the content to 'about.md'
    with open("../_pages/about.md", "w") as file:
        file.write(content)



def generate_indv_team_page_md(league, week, team, box_scores):
    weekly_scoring_chart = f"../assets/json/team_data/{team.team_abbrev}_{league.year}_weekly_scores.json"
    with open(weekly_scoring_chart, "r") as json_file:
        weekly_scores = json_file.read()
    # Ensure JSON is properly formatted
    parsed_weekly_scores = json.loads(weekly_scores)
    formatted_weekly_scores = json.dumps(parsed_weekly_scores, indent=4) 
    create_position_contribution_chart(team, week=None, through_week=week, box_scores=box_scores)
    pie_info = f"../assets/json/team_data/{team.team_abbrev}_2024_pie.json"
    with open(pie_info, "r") as json_file:
        pie_data = json_file.read()
    parsed_pie_data = json.loads(pie_data)
    formatted_pie_data = json.dumps(parsed_pie_data, indent=4) 
    content = f"""\
---
layout: page
title: {clean_team_name(team.team_name).lower()}
description: manager(s) - {get_manager_names(team.owners).lower()}
img: assets/img/{team.team_abbrev}_{league.year}.jpg
importance: {team.team_id+1}
category: {league.year}-{league.year-1999}
related_publications: false
chart:
  echarts: true
pretty_table: True
---

### <center> Through Week {week} </center>
<center>
<div class="row mb-3">
    <div class="col-12">
        <a href="/blog/{league.year}/Week-{week}-{team.team_abbrev}" class="btn btn-primary">Week {week} Recap</a>
    </div>
</div>
</center>

#### Summary
<table
data-click-to-select="true"
data-height="930"
data-search="false"
data-toggle="table"
data-url="{{{{ "/assets/json/team_data/{team.team_abbrev}_{league.year}_summary.json" }}}}">
<thead>
    <tr>
        <th data-field="category" data-halign="left" data-align="left" data-sortable="false">Category</th>
        <th data-field="value" data-halign="center" data-align="center" data-sortable="false">Value</th>
    </tr>
</thead>
</table>



<br><br>

```echarts
{formatted_weekly_scores}
```
<br><br>

#### Roster
<table
 data-click-to-select="true"
 data-height="1100"
 data-search="false"
 data-toggle="table"
 data-url="{{{{ "/assets/json/team_rosters/{team.team_abbrev}_{league.year}.json"}}}}">
 <thead>
   <tr>
     <th data-field="player_name" data-halign="left" data-align="left" data-sortable="false">Player</th>
     <th data-field="pos" data-halign="center" data-align="center" data-sortable="true">Position</th>
     <th data-field="total_points" data-halign="center" data-align="center" data-sortable="true">Total Points</th>
     <th data-field="proj_points" data-halign="center" data-align="center" data-sortable="true">Projected Points</th>
     <th data-field="avg_points" data-halign="center" data-align="center" data-sortable="true">Avg. Points</th>
     <th data-field="pct_perform" data-halign="center" data-align="center" data-sortable="true">Performance</th>
   </tr>
 </thead>
</table>

<br><br>

#### Positional Scoring
<table
data-click-to-select="true"
data-height="282"
data-search="false"
data-toggle="table"
data-url="{{{{ "/assets/json/team_data/{team.team_abbrev}_{league.year}_positions.json" }}}}">
<thead>
    <tr>
        <th data-field="position" data-halign="left" data-align="left" data-sortable="false">Position</th>
        <th data-field="average" data-halign="center" data-align="center" data-sortable="true">Average</th>
        <th data-field="highest" data-halign="center" data-align="center" data-sortable="true">Highest</th>
        <th data-field="lowest" data-halign="center" data-align="center" data-sortable="true">Lowest</th>
    </tr>
</thead>
</table>

<br><br>

```echarts
{formatted_pie_data}
```

#### Lineup Efficiency
<table
    data-click-to-select="true"
    data-height="810"
    data-search="false"
    data-toggle="table"
    data-url="{{{{ "/assets/json/team_data/{team.team_abbrev}_{league.year}_weekly.json" }}}}">
    <thead>
        <tr>
            <th data-field="week" data-halign="left" data-align="left" data-sortable="true">Week</th>
            <th data-field="efficiency" data-halign="center" data-align="center" data-sortable="true">Efficiency</th>
        </tr>
    </thead>
</table>

<br><br>

#### Draft Recap
<table
    data-click-to-select="true"
    data-height="1100"
    data-search="false"
    data-toggle="table"
    data-url="{{{{ "/assets/json/team_data/{team.team_abbrev}_{league.year}_draft.json" }}}}">
    <thead>
        <tr>
            <th data-field="round" data-halign="center" data-align="center" data-sortable="true">Round</th>
            <th data-field="pick" data-halign="center" data-align="center" data-sortable="false">Pick</th>
            <th data-field="draft_position" data-halign="center" data-align="center" data-sortable="true">Overall</th>
            <th data-field="player_name" data-halign="left" data-align="left" data-sortable="false">Player</th>
            <th data-field="points" data-halign="center" data-align="center" data-sortable="true">Total Points</th>
            <th data-field="grade" data-halign="center" data-align="center" data-sortable="true">Grade</th>
        </tr>
    </thead>
</table>

<br><br>
    
#### Head-to-Head Record
<table
    data-click-to-select="true"
    data-height="575"
    data-search="false"
    data-toggle="table"
    data-url="{{{{ "/assets/json/team_data/{team.team_abbrev}_{league.year}_h2h.json" }}}}">
    <thead>
        <tr>
            <th data-field="opponent" data-halign="left" data-align="left" data-sortable="false">Opponent</th>
            <th data-field="record" data-halign="center" data-align="center" data-sortable="true">Record</th>
            <th data-field="points" data-halign="center" data-align="center" data-sortable="false">Avg Score</th>
        </tr>
    </thead>
</table>
"""

    # Write the content to 'about.md'
    with open(f"../_projects/{team.team_abbrev}_{league.year}.md", "w") as file:
        file.write(content)
        
        
def generate_team_weekly_recap(league: League, team_name: str,box_scores, news_data: Dict,  week):
    # First find the team
    team = next((t for t in league.teams if clean_team_name(t.team_name) == team_name), None)
    create_position_contribution_chart(team, week=week, through_week=None, box_scores=box_scores)
    pie_info = f"../assets/json/team_data/{team.team_abbrev}_2024_Week_{week}_pie.json"
    with open(pie_info, "r") as json_file:
        pie_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_pie_data = json.loads(pie_data)
    formatted_pie_data = json.dumps(parsed_pie_data, indent=4) 
    
    if not team:
        raise ValueError(f"Team {team_name} not found")
    team_abbrev = team.team_abbrev    
    # Create markdown content
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    markdown_content = [f"""\
---
layout: post
title: {team_name} Week {week} Report
date: {current_date}
description: weekly team status recap
tags: 2024-25, WeeklyRecap, Week{week}
categories: team-reports
tabs: true
chart:
  echarts: true
pretty_table: = true
toc:
  sidebar: left
---"""]
    # After frontmatter but before injury report, add:
    box = next((b for b in box_scores[week] if b.home_team == team or b.away_team == team), None)
    standings = league.standings()
    current_rank = next((i for i, t in enumerate(standings, 1) if t.team_id == team.team_id), None)
    
    
    if box:
        opponent = box.home_team if box.away_team == team else box.away_team
        team_score = box.home_score if box.home_team == team else box.away_score
        opp_score = box.away_score if box.home_team == team else box.home_score
        result = "Won" if (box.home_team == team and team_score > opp_score) or \
                         (box.away_team == team and team_score > opp_score) else "Lost"
        
      # After getting box score but before adding to markdown_content
    weekly_effs, _, total_optimal_points, total_actual_points = get_efficiencies(week, box_scores, team)
    efficiency = (total_actual_points/total_optimal_points * 100) if total_optimal_points > 0 else 0
    
    # Get highest scoring player
    if box:
        lineup = box.home_lineup if box.home_team == team else box.away_lineup
        best_player = max(lineup, key=lambda x: x.points if x.slot_position != 'BE' else 0)
        
    # Get worst benching for this week
    worst_benchings = get_benchings(week, box_scores, [team])
    week_benchings = [b for b in worst_benchings.values() 
                     if b['week'] == week and 
                     b['team_name'] == clean_team_name(team.team_name)]
    worst_bench = max(week_benchings, key=lambda x: x['points_lost']) if week_benchings else None

    markdown_content.extend([
        "\n## Week at a Glance\n",
        f"{team_name} {result} against {clean_team_name(opponent.team_name)} "
        f"{team_score:.2f}-{opp_score:.2f}<br>",
        f"Current Standing: #{current_rank}<br>",
        f"Playoff Chances: {team.playoff_pct:.1f}%<br>",
        f"Lineup Efficiency: {efficiency:.1f}%<br>",
        f"Best Performer: {best_player.name} ({best_player.points:.2f} pts)<br>"
    ])

    if worst_bench and worst_bench['points_lost'] > 0:
        markdown_content.extend([
            f"Worst Benching: {worst_bench['benched_player']} "
            f"({worst_bench['benched_points']:.2f} pts) for {worst_bench['starter_player']} "
            f"({worst_bench['starter_points']:.2f} pts)<br>"
        ])
    markdown_content.append(f"""\
```echarts
{formatted_pie_data}
```""")        
    markdown_content.append("\n")
    # Filter news for this team
    team_news = []
    rostered_players = {player.name.lower(): {
        'name': player.name,
        'position': player.position,
        'lineup_slot': player.lineupSlot
    } for player in team.roster}
    markdown_content.extend(["\n## Player Report\n"])
    now = datetime.now(timezone.utc)
    last_update_time = datetime.strptime(news_data['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
    last_update_time = last_update_time.replace(tzinfo=timezone.utc)
    if now - last_update_time <= timedelta(days=4):
        for team_news in news_data.get('injuries', []):
            for news in team_news.get('injuries', []):
                player_name = news.get('athlete', {}).get('displayName', '').lower()
                if player_name in rostered_players:
                    markdown_content.extend([
                        f"#### {rostered_players[player_name]['name']} ({rostered_players[player_name]['position']})",
                        f"**Injury Status:** {news.get('status', 'Unknown')} <br>",
                        f"**Lineup Slot:** {rostered_players[player_name]['lineup_slot']} <br>",
                        f"**Details:** {news.get('longComment', '')}",
                    ])
    
    # Generate roster data for JSON
    roster_data = []
    optimal_data = []
    
    box = next((b for b in box_scores[week] if b.home_team == team or b.away_team == team), None)
    if box:
        lineup = box.home_lineup if box.home_team == team else box.away_lineup
        starters = [p for p in lineup if p.slot_position != 'BE' and p.slot_position != 'IR']
        all_players = lineup
        
        # Current roster performance
        for player in starters:
            player_data = {
                "player_name": player.name,
                "pos": player.position,
                "slot": player.slot_position,
                "points": player.points,
                "projected": player.projected_points
            }
            roster_data.append(player_data)
        
        # Calculate optimal lineup using _get_efficiencies logic
        optimal_points = 0
        pos_requirements = {}
        for player in starters:
            if player.slot_position in pos_requirements:
                pos_requirements[player.slot_position] += 1
            else:
                pos_requirements[player.slot_position] = 1
        
        priority_pos = ['QB', 'WR', 'RB', 'TE', 'RB/WR/TE', 'OP']
        pos_requirements = sort_dict_with_prioritized_keys(pos_requirements, priority_keys=priority_pos)
        all_players = sorted(all_players, key=lambda x: x.points, reverse=True)
        used_players = set()

        # Fill each position with best available players
        for pos, count in pos_requirements.items():
            eligible = [p for p in all_players 
                       if pos in p.eligibleSlots 
                       and p.name not in used_players]
            
            for player in eligible[:count]:
                optimal_points += player.points
                player_data = {
                    "player_name": player.name,
                    "pos": player.position,
                    "slot": pos,
                    "points": player.points,
                    "projected": player.projected_points
                }
                optimal_data.append(player_data)
                used_players.add(player.name)
    
    # Save JSON data
    nfl_week = week
    nfl_year = league.year
    json_filename = f"Week_{nfl_week}_{nfl_year}_{team.team_abbrev}_roster.json"
    optimal_filename = f"Week_{nfl_week}_{nfl_year}_{team.team_abbrev}_optimal.json"
    markdown_filename = f"{datetime.now().strftime('%Y-%m-%d')}-Week-{nfl_week}-{team.team_abbrev}.md"
    os.makedirs(f"../assets/json/team_rosters", exist_ok=True)
    
    with open(f"../assets/json/team_rosters/{json_filename}", 'w') as f:
        json.dump(roster_data, f, indent=2)
    
    with open(f"../assets/json/team_rosters/{optimal_filename}", 'w') as f:
        json.dump(optimal_data, f, indent=2)
    

    os.makedirs(f"../_posts", exist_ok=True)
    # Add tables to markdown
    markdown_content.extend([
        "\n## Current Lineup\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"630\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        f"data-url=\"{{{{ \"/assets/json/team_rosters/{json_filename}\"}}}}\">",
        "<thead>",
        "<tr>",
        "<th data-field=\"player_name\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\">Player</th>",
        "<th data-field=\"pos\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Position</th>",
        "<th data-field=\"slot\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Slot</th>",
        "<th data-field=\"points\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Points</th>",
        "<th data-field=\"projected\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Projected</th>",
        "</tr>",
        "</thead>",
        "</table>\n",
        "<br><br>"
        "\n## Optimal Lineup\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"630\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        f"data-url=\"{{{{ \"/assets/json/team_rosters/{optimal_filename}\"}}}}\">",
        "<thead>",
        "<tr>",
        "<th data-field=\"player_name\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\">Player</th>",
        "<th data-field=\"pos\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Position</th>",
        "<th data-field=\"slot\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Slot</th>",
        "<th data-field=\"points\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Points</th>",
        "<th data-field=\"projected\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Projected</th>",
        "</tr>",
        "</thead>",
        "</table>"
    ])
    
    
    with open(f"../_posts/{markdown_filename}", 'w') as f:
        f.write('\n'.join(markdown_content))
        
def generate_league_weekly_recap_markdown(league: League, box_scores, week):
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nfl_week = week
    nfl_year = league.year
    generate_echarts_heatmap_weekly_json(league.teams, box_scores, week)
    markdown_content = [
        "---",
        "layout: post",
        f"title: Week {week} League Recap",
        f"date: {current_date}",
        "description: Weekly league recap and standings",
        f"tags: 2024-25, WeeklyRecap, Week{week}",
        "categories: league-recaps",
        "tabs: true",
        "pretty_table: true",f"""\
chart:
  echarts: true
toc:
  sidebar: left""",
        "---",
        "\n### Weekly Matchups\n"
    ]
    
    # Get box scores and standings
    pos_data_path = "../assets/json/weekly_heatmap_config.json"
    with open(pos_data_path, "r") as json_file:
        pos_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_pos_json = json.loads(pos_data)
    formatted_pos_json = json.dumps(parsed_pos_json, indent=4)
    standings = league.standings()
    total_points_in_week = 0
    # Process each matchup
    for box in box_scores[week]:
        if not box.away_team:  # Skip bye weeks
            continue
            
        # Get matchup scores
        home_score = box.home_score
        away_score = box.away_score
        total_points_in_week += home_score
        total_points_in_week+= away_score
        
        # Get highest scoring player in matchup
        all_players = box.home_lineup + box.away_lineup
        best_player = max(all_players, key=lambda x: x.points if x.slot_position != 'BE' else 0)
        best_player_team = box.home_team if best_player in box.home_lineup else box.away_team
        
        # Get worst benchings for both teams
        worst_benchings = get_benchings(week, box_scores, [box.home_team, box.away_team])
        matchup_benchings = [b for b in worst_benchings.values() 
                           if b['week'] == week and 
                           (b['team_name'] in [clean_team_name(box.home_team.team_name), 
                                             clean_team_name(box.away_team.team_name)])]
        worst_bench = max(matchup_benchings, key=lambda x: x['points_lost']) if matchup_benchings else None
        
        markdown_content.extend([
            f"#### {clean_team_name(box.away_team.team_name)} @ {clean_team_name(box.home_team.team_name)}\n",
            f"**Final Score:** {clean_team_name(box.away_team.team_name)} {away_score:.2f} - "
            f"{home_score:.2f} {clean_team_name(box.home_team.team_name)}<br>",
            f"**Best Performance:** {best_player.name} ({clean_team_name(best_player_team.team_name)}) - "
            f"{best_player.points:.2f} pts<br>"
        ])
        
        if worst_bench and worst_bench['points_lost'] > 0:
            markdown_content.extend([
                f"**Worst Benching:** {worst_bench['team_name']} benched {worst_bench['benched_player']} "
                f"({worst_bench['benched_points']:.2f} pts) for {worst_bench['starter_player']} "
                f"({worst_bench['starter_points']:.2f} pts)<br>"
            ])
        
        markdown_content.append("\n")
    
    def biggest_overachiever(matchups):
        overachievers = []
        for matchup in matchups:
            # Handle home team
            home_team = matchup.home_team
            if home_team and hasattr(matchup, 'home_score') and hasattr(matchup, 'home_projected'):
                overachievers.append((home_team.team_name, matchup.home_score - matchup.home_projected))
            
            # Handle away team
            away_team = matchup.away_team
            if away_team and hasattr(matchup, 'away_score') and hasattr(matchup, 'away_projected'):
                overachievers.append((away_team.team_name, matchup.away_score - matchup.away_projected))
        
        # Find the biggest overachiever
        return max(overachievers, key=lambda x: x[1])

    def biggest_underachiever(matchups):
        underachievers = []
        for matchup in matchups:
            # Handle home team
            home_team = matchup.home_team
            if home_team and hasattr(matchup, 'home_score') and hasattr(matchup, 'home_projected'):
                underachievers.append((home_team.team_name, matchup.home_score - matchup.home_projected))
            
            # Handle away team
            away_team = matchup.away_team
            if away_team and hasattr(matchup, 'away_score') and hasattr(matchup, 'away_projected'):
                underachievers.append((away_team.team_name, matchup.away_score - matchup.away_projected))
        
        # Find the biggest underachiever
        return min(underachievers, key=lambda x: x[1])


    # Find the biggest overachiever and underachiever
    overachiever = biggest_overachiever(box_scores[week])
    underachiever = biggest_underachiever(box_scores[week])
    markdown_content.extend(["<br>",
        f"### League Info \n",
        f"**Total Points Scored:** {total_points_in_week:.2f} <br>",
        f"**Avg. Points Scored:** {total_points_in_week/len(league.teams):.2f}<br>",
        f"**Biggest Overachiever:** {overachiever[0]} exceeded projections by {overachiever[1]:.2f} points (THIS IS JUST BC OF 2 WEEK PLAYOFFS)<br>",
        f"**Biggest Underachiever:** {underachiever[0]} fell short of projections by {underachiever[1]:.2f} points (THIS IS JUST BC OF 2 WEEK PLAYOFFS)"
    ])
    # Create standings data for JSON
    standings_data = []
    for rank, team in enumerate(standings, 1):
        standings_data.append({
            "rank": rank,
            "team": clean_team_name(team.team_name),
            "record": f"{team.wins}-{team.losses}",
            "record_sort": f"{team.wins / (team.wins + team.losses)}",
            "points_for": f"{team.points_for:.2f}",
            "playoff_odds": f"{team.playoff_pct:.1f}%"
        })
    markdown_content.append("\n")
    # Save standings JSON
    standings_filename = f"Week_{week}_{nfl_year}_standings.json"
    os.makedirs(f"../assets/json/standings", exist_ok=True)
    with open(f"../assets/json/standings/{standings_filename}", 'w') as f:
        json.dump(standings_data, f, indent=2)

    # Replace the markdown standings table with bootstrap table
    markdown_content.extend([
        "## Current Standings\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"635\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        f"data-url=\"{{{{ \"/assets/json/standings/{standings_filename}\"}}}}\">",
        "<thead>",
        "<tr>",
        "<th data-field=\"rank\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Rank</th>",
        "<th data-field=\"team\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\">Team</th>",
        "<th data-field=\"record\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\" data-sort-name=\"record_sort\">Record</th>",
        "<th data-field=\"record_sort\" data-sortable=\"true\" data-visible=\"false\">Record Sort</th>",
        "<th data-field=\"points_for\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Points For</th>",
        "<th data-field=\"playoff_odds\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Playoff Odds</th>",
        "</tr>",
        "</thead>",
        "</table>\n"
    ])
    markdown_content.append(f"""\
<br>
## Positional Scoring This Week
```echarts
{formatted_pos_json}
```
    """)
    markdown_content.append(f"## Week {week+1} Preview:")
    for i in range(int(len(league.teams)/2)):
        markdown_content.extend([
                f"#### {clean_team_name(league.box_scores(week+1)[i].away_team.team_name)} @ {clean_team_name(league.box_scores(week+1)[i].home_team.team_name)}\n",
                f"**Projected Score:** {clean_team_name(league.box_scores(week+1)[i].away_team.team_name)} {league.box_scores(week+1)[i].away_projected:.2f} - "
            f"{league.box_scores(week+1)[i].home_projected:.2f} {clean_team_name(league.box_scores(week+1)[i].home_team.team_name)}<br>",
            
        ])
        markdown_content.append("\n")
    # Save markdown file
    markdown_filename = f"{datetime.now().strftime('%Y-%m-%d')}-Week-{week}_Recap.md"
    os.makedirs(f"../_posts", exist_ok=True)
    with open(f"../_posts/{markdown_filename}", 'w') as f:
        f.write('\n'.join(markdown_content))
        
        
def generate_draft_page():
    # Read existing JSON data
    with open("../assets/json/team_data/draft_total_2024.json", 'r') as f:
        all_picks = json.load(f)
    
    # Sort and get best and worst picks
    best_picks = sorted(all_picks, key=lambda x: float(x['value_diff']), reverse=True)[:5]
    worst_picks = sorted(all_picks, key=lambda x: float(x['value_diff']))[:5]
    
    # Save filtered JSON files
    os.makedirs("../assets/json/team_data", exist_ok=True)
    
    with open("../assets/json/team_data/draft_best_2024.json", 'w') as f:
        json.dump(best_picks, f, indent=2)
    
    with open("../assets/json/team_data/draft_worst_2024.json", 'w') as f:
        json.dump(worst_picks, f, indent=2)

    # Create markdown content with the same format as original
    content = [
        "---",
        "layout: page",
        "permalink: /draft/",
        "title: draft",
        "nav: true",
        "nav_order: 4",
        "description:",
        "chart:",
        "echarts: true",
        "pretty_table: True",
        "---",
        "\n## Best Draft Picks\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"340\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        "data-url=\"{{ \"/assets/json/team_data/draft_best_2024.json\" }}\">",
        "<thead>",
        "<tr>",
        "<th data-field=\"team\" data-halign=\"center\" data-align=\"left\" data-sortable=\"true\">Team</th>",
        "<th data-field=\"round\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Round</th>",
        "<th data-field=\"pick\" data-halign=\"center\" data-align=\"center\" data-sortable=\"false\">Pick</th>",
        "<th data-field=\"draft_position\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Overall</th>",
        "<th data-field=\"player_name\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\">Player</th>",
        "<th data-field=\"grade\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Grade</th>",
        "</tr>",
        "</thead>",
        "</table><br>\n",
        "\n## Worst Draft Picks\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"340\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        "data-url=\"{{ \"/assets/json/team_data/draft_worst_2024.json\" }}\">",
        "<thead>",
        "<tr>",
        "<th data-field=\"team\" data-halign=\"center\" data-align=\"left\" data-sortable=\"true\">Team</th>",
        "<th data-field=\"round\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Round</th>",
        "<th data-field=\"pick\" data-halign=\"center\" data-align=\"center\" data-sortable=\"false\">Pick</th>",
        "<th data-field=\"draft_position\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Overall</th>",
        "<th data-field=\"player_name\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\">Player</th>",
        "<th data-field=\"grade\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Grade</th>",
        "</tr>",
        "</thead>",
        "</table><br>\n",
        "\n## All Draft Picks\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"800\"",
        "data-search=\"true\"",
        "data-toggle=\"table\"",
        "data-url=\"{{ \"/assets/json/team_data/draft_total_2024.json\" }}\">",
        "<thead>",
        "<tr>",
        "<th data-field=\"team\" data-halign=\"center\" data-align=\"left\" data-sortable=\"true\">Team</th>",
        "<th data-field=\"round\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Round</th>",
        "<th data-field=\"pick\" data-halign=\"center\" data-align=\"center\" data-sortable=\"false\">Pick</th>",
        "<th data-field=\"draft_position\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Overall</th>",
        "<th data-field=\"player_name\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\">Player</th>",
        "<th data-field=\"grade\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Grade</th>",
        "</tr>",
        "</thead>",
        "</table>"
    ]

    # Save markdown file
    os.makedirs("../_pages", exist_ok=True)
    with open(f"../_pages/draft.md", 'w') as f:
        f.write('\n'.join(content))
        

def generate_players_page(league: League, week):
    positions = ['QB', 'RB', 'WR', 'TE']
    players_by_pos = {pos: [] for pos in positions}
    
    # Load existing draft data
    with open("../assets/json/team_data/draft_total_2024.json", 'r') as f:
        draft_data = json.load(f)
        
    # Create draft lookup dictionary
    draft_lookup = {pick['player_name']: {
        'draft': f"{pick['round']}.{pick['pick']}", 
        'overall_pick': pick['draft_position']
    } for pick in draft_data}
    
    # Get all rostered players data
    for team in league.teams:
        for player in team.roster:
            if player.position in positions:
                # Get draft info from lookup
                draft_info = draft_lookup.get(player.name, {'draft': 'FA', 'overall_pick': 999})
                
                # Scale projected points to current week
                scaled_projection = player.projected_total_points / 17 * week

                player_data = {
                    "player_name": player.name,
                    "team": clean_team_name(team.team_name),
                    "draft": draft_info['draft'],
                    "overall_pick": draft_info['overall_pick'],
                    "points": player.total_points,
                    "projected": round(scaled_projection, 2)
                }
                players_by_pos[player.position].append(player_data)

    # Sort each position by points and save top 10
    os.makedirs("../assets/json/players", exist_ok=True)
    for pos in positions:
        top_players = sorted(players_by_pos[pos], key=lambda x: x['points'], reverse=True)[:10]
        with open(f"../assets/json/players/top_{pos.lower()}_2024.json", 'w') as f:
            json.dump(top_players, f, indent=2)

     # Generate markdown content
    content = [
        "---",
        "layout: page",
        "permalink: /players/",
        "title: players",
        "nav: false",
        "nav_order: 3",
        "description: Top performers at each position",
        "chart:",
        "echarts: true",
        "pretty_table: True",
        "---"
    ]
    # Get top scorers at each position for summary
    top_scorers = {pos: sorted(players_by_pos[pos], key=lambda x: x['points'], reverse=True)[0] 
                   for pos in positions}
    
    content.extend([
        "\n### Season Overview\n",
        "Leading the way this season:\n",
        f"* **QB:** {top_scorers['QB']['player_name']} ({top_scorers['QB']['points']} pts) owned by {top_scorers['QB']['team']}\n",
        f"* **RB:** {top_scorers['RB']['player_name']} ({top_scorers['RB']['points']} pts) owned by {top_scorers['RB']['team']}\n",
        f"* **WR:** {top_scorers['WR']['player_name']} ({top_scorers['WR']['points']} pts) owned by {top_scorers['WR']['team']}\n",
        f"* **TE:** {top_scorers['TE']['player_name']} ({top_scorers['TE']['points']} pts) owned by {top_scorers['TE']['team']}\n\n",
        "Below are the top 10 performers at each position through Week " + str(week) + ".\n\n"
    ])
    # Add a table for each position
    for pos in positions:
        content.extend([
            f"\n## Top {pos}s\n",
            "<table",
            "data-click-to-select=\"true\"",
            "data-height=\"635\"",
            "data-search=\"false\"",
            "data-toggle=\"table\"",
            f"data-url=\"{{{{ \"/assets/json/players/top_{pos.lower()}_2024.json\" }}}}\">",
            "<thead>",
            "<tr>",
            "<th data-field=\"player_name\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\">Player</th>",
            "<th data-field=\"team\" data-halign=\"center\" data-align=\"left\" data-sortable=\"true\">Team</th>",
            "<th data-field=\"draft\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\" data-sort-name=\"overall_pick\">Draft</th>",
            "<th data-field=\"overall_pick\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\" data-visible=\"false\">Overall</th>",
            "<th data-field=\"points\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Points</th>",
            "<th data-field=\"projected\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Projected</th>",
            "</tr>",
            "</thead>",
            "</table><br>\n"
        ])

    # Save markdown file
    os.makedirs("../_pages", exist_ok=True)
    with open(f"../_pages/players.md", 'w') as f:
        f.write('\n'.join(content))
        
def generate_records_page():
    content = [
        "---",
        "layout: default",
        "permalink: /records/",
        "title: records",
        "nav: false",
        "nav_order: 7",
        "description: All-time league records and notable achievements",
        "chart:",
        "echarts: true",
        "pretty_table: True",
        "---",

        
        "\n## Single Game Records\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        "data-url=\"{{ \"/assets/json/records/game_records.json\" }}\"",
        "data-show-footer=\"false\">",  # Added to remove bottom line
        "<thead>",
        "<tr>",
        "<th data-field=\"category\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\" data-width=\"200\">Record</th>",
        "<th data-field=\"value\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\" data-width=\"100\">Value</th>",
        "<th data-field=\"details\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\" data-width=\"300\">Details</th>",
        "<th data-field=\"year\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\" data-width=\"100\">Year</th>",
        "</tr>",
        "</thead>",
        "</table><br>\n",
        
        "\n## Season Records\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        "data-url=\"{{ \"/assets/json/records/season_records.json\" }}\"",
        "data-show-footer=\"false\">",  # Added to remove bottom line
        "<thead>",
        "<tr>",
        "<th data-field=\"category\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\" data-width=\"200\">Record</th>",
        "<th data-field=\"value\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\" data-width=\"100\">Value</th>",
        "<th data-field=\"team\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\" data-width=\"200\">Team</th>",
        "<th data-field=\"year\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\" data-width=\"100\">Year</th>",
        "</tr>",
        "</thead>",
        "</table><br>\n",
        
        "\n## Positional Records\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        "data-url=\"{{ \"/assets/json/records/position_records.json\" }}\"",
        "data-show-footer=\"false\">",  # Added to remove bottom line
        "<thead>",
        "<tr>",
        "<th data-field=\"category\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\" data-width=\"200\">Record</th>",
        "<th data-field=\"value\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\" data-width=\"100\">Value</th>",
        "<th data-field=\"player\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\" data-width=\"200\">Player</th>",
        "<th data-field=\"team\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\" data-width=\"200\">Team</th>",
        "<th data-field=\"year\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\" data-width=\"100\">Year</th>",
        "</tr>",
        "</thead>",
        "</table>\n"
    ]

    os.makedirs("../_pages", exist_ok=True)
    with open(f"../_pages/records.md", 'w') as f:
        f.write('\n'.join(content))
        
def generate_history_page():
    content = [
        "---",
        "layout: page",
        "permalink: /teamhistory/",
        "title: team history",
        "nav: false",
        "nav_order: 6",
        "description: Historical record of teams and managers",
        "chart:",
        "echarts: true",
        "pretty_table: True",
        "---",
        "\n# League History\n <br>"
    ]

    # Get list of years from the files in the history directory
    history_files = glob.glob("../assets/json/history/*_teams.json")
    years = sorted([int(f.split('/')[-1].split('_')[0]) for f in history_files], reverse=True)

    for year in years:
        content.extend([
            f"\n## {year} Season\n",
            "<table",
            "data-click-to-select=\"true\"",
            "data-height=\"400\"",
            "data-search=\"false\"",
            "data-toggle=\"table\"",
            f"data-url=\"{{{{ \"/assets/json/history/{year}_teams.json\" }}}}\">",
            "<thead>",
            "<tr>",
            "<th data-field=\"team_name\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\">Team</th>",
            "<th data-field=\"managers\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\">Managers</th>",
            "<th data-field=\"final_rank\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Final Rank</th>",
            "<th data-field=\"record\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Record</th>",
            "<th data-field=\"points\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Points</th>",
            "</tr>",
            "</thead>",
            "</table>\n"
        ])

    os.makedirs("../_pages", exist_ok=True)
    with open(f"../_pages/teamhistory.md", 'w') as f:
        f.write('\n'.join(content))
        
        
def generate_waivers_page(league, waiver_adds, fa_adds, trades):    
    generate_best_pickups_json(league, waiver_adds, fa_adds, trades)
    generate_all_transactions_json(league, waiver_adds, fa_adds)
    content = f"""\
---
layout: page
permalink: /waivers/
title: waivers
nav: false
nav_order: 4
description:
chart:
    echarts: true
pretty_table: True
---

### Best Pickups
<table
data-click-to-select="true"
data-height="930"
data-search="false"
data-toggle="table"
data-url="{{{{ "/assets/json/transactions/best_fa_{league.year}.json"}}}}">
<thead>
    <tr>
     <th data-field="player_name" data-halign="left" data-align="left" data-sortable="false">Player</th>
     <th data-field="team" data-halign="center" data-align="center" data-sortable="false">Acquiring Team</th>
     <th data-field="position" data-halign="center" data-align="center" data-sortable="false">Position</th>
     <th data-field="week" data-halign="center" data-align="center" data-sortable="false">Week</th>
     <th data-field="points_after" data-halign="center" data-align="center" data-sortable="true">Points Since Acquiring</th>
     <th data-field="type" data-halign="center" data-align="center" data-sortable="true">FA or Waiver</th>
    </tr>
</thead>
</table>
<br>
### All Pickups
<table
data-click-to-select="true"
data-height="930"
data-search="false"
data-toggle="table"
data-url="{{{{ "/assets/json/transactions/all_fa_{league.year}.json"}}}}">
<thead>
    <tr>
     <th data-field="player_name" data-halign="left" data-align="left" data-sortable="false">Player</th>
     <th data-field="team" data-halign="center" data-align="center" data-sortable="true">Acquiring Team</th>
     <th data-field="position" data-halign="center" data-align="center" data-sortable="true">Position</th>
     <th data-field="week" data-halign="center" data-align="center" data-sortable="true">Week</th>
     <th data-field="type" data-halign="center" data-align="center" data-sortable="true">FA or Waiver</th>
    </tr>
</thead>
</table>
"""
    os.makedirs("../_pages", exist_ok=True)
    with open(f"../_pages/free_agency.md", 'w') as f:
        f.write(content)
        
def generate_trades_page(league, trades):    
    generate_trades_json(league, trades)
    generate_trade_network_json(league, trades)
    trade_info = f"../assets/json/transactions/network_trades_{league.year}.json"
    with open(trade_info, "r") as json_file:
        trade_data = json_file.read()
    # Ensure JSON is properly formatted
    parsed_trade_data = json.loads(trade_data)
    formatted_trade_data = json.dumps(parsed_trade_data, indent=4) 
    content = f"""\
---
layout: page
permalink: /trades/
title: trades
nav: false
nav_order: 5
description:
chart:
    echarts: true
pretty_table: True
---

<center>
<div class="row mb-3">
    <div class="col-12">
        <a href="trade_analyzer" class="btn btn-primary ">Trade Analyzer</a>
        <a href="trade_suggestions" class="btn btn-primary">Trade Suggestions</a>
    </div>
</div>
</center>



### All Trades
<table
data-click-to-select="true"
data-height="520"
data-search="false"
data-toggle="table"
data-url="{{{{ "/assets/json/transactions/trades_{league.year}.json"}}}}">
<thead>
    <tr>
     <th data-field="week" data-halign="left" data-align="left" data-sortable="true">Week</th>
     <th data-field="team_1" data-halign="center" data-align="center" data-sortable="true">Team 1</th>
     <th data-field="team_1_sending" data-halign="center" data-align="center" data-sortable="false">Sending</th>
     <th data-field="team_2" data-halign="center" data-align="center" data-sortable="false">Team 2</th>
     <th data-field="team_2_sending" data-halign="center" data-align="center" data-sortable="true">Sending</th>
    </tr>
</thead>
</table>
<br>
```echarts
{formatted_trade_data}
```

"""
    os.makedirs("../_pages", exist_ok=True)
    with open(f"../_pages/trades.md", 'w') as f:
        f.write(content)
        
        
def generate_playoff_page(league, week):
    num_playoff_teams = league.settings.playoff_team_count
    playoff_teams = sorted(league.teams, 
                         key=lambda x: x.final_standing if x.final_standing != 0 else x.standing,
                         reverse=False)[:num_playoff_teams]
    teams = playoff_teams
    
    # Clean team names and get their scores for the given week
    team_0_name = clean_team_name(teams[0].team_name)
    team_0_score = teams[0].scores[week-1]

    team_3_name = clean_team_name(teams[3].team_name)
    team_3_score = teams[3].scores[week-1]

    team_1_name = clean_team_name(teams[1].team_name)
    team_1_score = teams[1].scores[week-1]

    team_2_name = clean_team_name(teams[2].team_name)
    team_2_score = teams[2].scores[week-1]
    
    # Create the content using an f-string
    content = f"""\
---
layout: page
permalink: /playoffs/
title: playoffs
description: 
nav: true
nav_order: 7
chart:
  echarts: true
---


```echarts
{{
  "series": [
    {{
      "type": "tree",
      "data": [
        {{
          "name": "Finals",
          "symbol": "rect",
          "symbolSize": [250, 50],
          "children": [
            {{
              "name": "Winner of Semifinal 1",
              "symbol": "rect",
              "symbolSize": [250, 50],
              "children": [
                {{
                  "name": "{team_0_name}",
                  "value": "{team_0_score}",
                  "itemStyle": {{
                    "color": "#7EC8B6"
                  }},
                  "symbol": "rect",
                  "symbolSize": [250, 50],
                  "label": {{
                    "formatter": "{{b}}\\n{{c}}"
                  }}
                }},
                {{
                  "name": "{team_3_name}",
                  "value": "{team_3_score}",
                  "itemStyle": {{
                    "color": "#FF6347"
                  }},
                  "symbol": "rect",
                  "symbolSize": [250, 50],
                  "label": {{
                    "formatter": "{{b}}\\n{{c}}"
                  }}
                }}
              ]
            }},
            {{
              "name": "Winner of Semifinal 2",
              "symbol": "rect",
              "symbolSize": [250, 50],
              "children": [
                {{
                  "name": "{team_1_name}",
                  "value": "{team_1_score}",
                  "itemStyle": {{
                    "color": "#FFD700"
                  }},
                  "symbol": "rect",
                  "symbolSize": [250, 50],
                  "label": {{
                    "formatter": "{{b}}\\n{{c}}"
                  }}
                }},
                {{
                  "name": "{team_2_name}",
                  "value": "{team_2_score}",
                  "itemStyle": {{
                    "color": "#1E90FF"
                  }},
                  "symbol": "rect",
                  "symbolSize": [250, 50],
                  "label": {{
                    "formatter": "{{b}}\\n{{c}}"
                  }}
                }}
              ]
            }}
          ]
        }}
      ],
      "orient": "RL",
      "top": "5%",
      "left": "15%",
      "bottom": "5%",
      "right": "15%",
      "label": {{
        "position": "inside",
        "verticalAlign": "middle",
        "align": "center",
        "fontSize": 16
      }},
      "lineStyle": {{
        "color": "#555",
        "width": 2
      }}
    }}
  ]
}}
```"""
    os.makedirs("../_pages", exist_ok=True)
    with open(f"../_pages/playoffs.md", 'w') as f:
        f.write(content)
        
def generate_trade_analyzer_page():
    content = f"""\
---
layout: page
permalink: /trades/trade_analyzer/
title: trade analyzer
nav: false
nav_order: 6
custom_js:
    - trade-analyzer
description: Analyze potential trades using projections and historical data
chart:
    echarts: true
pretty_table: True
---

<script src="../../assets/js/trade-analyzer.js"></script>

<div class="container mt-4">
...

<div class="container mt-4">
    <div class="row">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>Team 1</h5>
                </div>
                <div class="card-body">
                    <select id="team1-select" class="form-control mb-3">
                        <option value="">Select Team</option>
                    </select>
                    <select id="team1-players" class="form-control" multiple size="8">
                    </select>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>Team 2</h5>
                </div>
                <div class="card-body">
                    <select id="team2-select" class="form-control mb-3">
                        <option value="">Select Team</option>
                    </select>
                    <select id="team2-players" class="form-control" multiple size="8">
                    </select>
                </div>
            </div>
        </div>
    </div>
    
    <div class="row mt-3">
        <div class="col-12 text-center">
            <button id="analyze-btn" class="btn btn-primary">Analyze Trade</button>
        </div>
    </div>

    <div id="analysis-results" class="mt-4" style="display:none;">
        <div class="row">
            <div class="col-md-6">
                <div id="team1-analysis" class="card">
                </div>
            </div>
            <div class="col-md-6">
                <div id="team2-analysis" class="card">
                </div>
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-12">
                <div id="trade-chart"></div>
            </div>
        </div>
    </div>
</div>
"""
    
    os.makedirs("../_pages", exist_ok=True)
    with open("../_pages/trade_analyzer.md", "w") as f:
        f.write(content)
        
def generate_matchups_preview(league, week, box_scores, news_data):
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    markdown_content = [
        "---",
        "layout: post",
        f"title: Week {week+1} Matchups Preview",
        f"date: {current_date}",
        "description: preview of next weeks matchups",
        f"tags: 2024-25, WeeklyPreview, Week{week+1}",
        "categories: league-previews",
        "tabs: true",
        "pretty_table: true",f"""\
chart:
  echarts: true
toc:
  sidebar: left
  max_level: 2""",
        "---"
    ]

    matchups = league.box_scores(week+1)
    
    for matchup in matchups:
        if not matchup.away_team:  # Skip bye weeks
            continue
            
        home_team = matchup.home_team
        away_team = matchup.away_team
        
        # Inside the main matchup loop, after getting home_team and away_team:

        # Add recent performance trends
        home_recent = home_team.scores[max(0, week-3):week]
        away_recent = away_team.scores[max(0, week-3):week]
        home_trend = sum(home_recent)/len(home_recent) if home_recent else 0
        away_trend = sum(away_recent)/len(away_recent) if away_recent else 0

        # Get streaks
        _, _, home_streak_len, home_streak_type = get_streaks(home_team.outcomes[:week])
        _, _, away_streak_len, away_streak_type = get_streaks(away_team.outcomes[:week])

        # Get previous matchup results this season
        previous_matchups = []
        for w, (opp, score) in enumerate(zip(home_team.schedule[:week], home_team.scores[:week])):
            if opp.team_id == away_team.team_id:
                previous_matchups.append((w+1, score, opp.scores[w]))

        # Get playoff implications
        home_playoff_odds = home_team.playoff_pct
        away_playoff_odds = away_team.playoff_pct

        
        
        # Get historical h2h records and stats
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
        
        # Get position comparisons
        home_pos_stats = get_positional_scoring_amounts(box_scores, week, home_team)
        away_pos_stats = get_positional_scoring_amounts(box_scores, week, away_team)
        if avg_home_score > avg_away_score:
            historical_winner = clean_team_name(home_team.team_name)
        elif avg_home_score < avg_away_score:
            historical_winner = clean_team_name(away_team.team_name)
        else:
            historical_winner = "How did y'all even manage this"
        markdown_content.extend([
            f"### {clean_team_name(away_team.team_name)} @ {clean_team_name(home_team.team_name)}\n",
            f"**Projected Score:** {clean_team_name(away_team.team_name)} {matchup.away_projected:.2f} - "
            f"{matchup.home_projected:.2f} {clean_team_name(home_team.team_name)}\n",
            f"**Historical Matchup:** {h2h_wins}-{total_games-h2h_wins} "
            f"(Avg Score: {historical_winner} wins by {avg_home_score:.1f}-{avg_away_score:.1f}) \n"
        ])
        
        # Replace the existing position breakdown table with:
        markdown_content.extend([
            "\n#### Position Breakdown\n",
            "<table class='table table-bordered'>",
            "<thead>",
            "<tr>",
            "<th style='width: 20%'>Position</th>",
            f"<th style='width: 35%'>{clean_team_name(away_team.team_name)}</th>",
            "<th style='width: 10%'></th>",  # For the arrow
            f"<th style='width: 35%'>{clean_team_name(home_team.team_name)}</th>",
            "</tr>",
            "</thead>",
            "<tbody>"
        ])

        for pos in get_non_flex_positions(box_scores, 1):
            away_avg = sum(away_pos_stats.get(pos, [0]))/len(away_pos_stats.get(pos, [1]))
            home_avg = sum(home_pos_stats.get(pos, [0]))/len(home_pos_stats.get(pos, [1]))

            # Determine advantage
            diff = away_avg - home_avg
            # if abs(diff) < 0.5:
            #     arrow = "↔️"  # Even matchup
            if diff < 0:
                arrow = "➡️"  # Advantage to away team
            else:
                arrow = "⬅️"  # Advantage to home team
                
            markdown_content.append(
                f"<tr><td><strong>{pos}</strong></td>"
                f"<td>{away_avg:.1f}</td>"
                f"<td>{arrow}</td>"
                f"<td>{home_avg:.1f}</td></tr>"
            )

        markdown_content.append("</tbody></table>\n <br>")

        # After the position breakdown table but before injuries:

        scoring_chart, radar_chart = create_matchup_charts(home_team, away_team, week, box_scores)

        markdown_content.extend([
            "\n#### Recent Performance\n",
            "```echarts",
            json.dumps(scoring_chart, indent=2),
            "```\n",
            "\n#### Position Comparison\n",
            "```echarts",
            json.dumps(radar_chart, indent=2),
            "```\n"
        ])
        
        markdown_content.append("\n\n#### Injury Report\n\n")
        # Add injury report if available
        markdown_content.extend([f"**{home_team.team_name}:** "])
        if news_data:
            for team_news in news_data.get('injuries', []):
                for news in team_news.get('injuries', []):
                    player_name = news.get('athlete', {}).get('displayName', '').lower()
                    if any(player_name == p.name.lower() for p in home_team.roster):
                        if news.get('status', '') != 'Active':
                            markdown_content.extend([
                                f"{news.get('athlete', {}).get('displayName', '')} "
                                f"({news.get('status', '')}), "
                            ])
        markdown_content.extend([f" \n**{away_team.team_name}:** "])
        if news_data:
            for team_news in news_data.get('injuries', []):
                for news in team_news.get('injuries', []):
                    player_name = news.get('athlete', {}).get('displayName', '').lower()
                    if any(player_name == p.name.lower() for p in away_team.roster):
                        if news.get('status', '') != 'Active':
                            markdown_content.extend([
                                f"{news.get('athlete', {}).get('displayName', '')} "
                                f"({news.get('status', '')}), "
                            ])
        
        # Add to markdown content:
        markdown_content.extend([
            f"\n#### Recent Form",
            f"**{clean_team_name(home_team.team_name)}:** {home_trend:.1f} ppg last 3 weeks ({home_streak_len} game {home_streak_type} streak) \n",
            f"**{clean_team_name(away_team.team_name)}:** {away_trend:.1f} ppg last 3 weeks ({away_streak_len} game {away_streak_type} streak)\n",
            
            "\n#### Previous Matchups This Season",
            *[f"Week {week}: {clean_team_name(home_team.team_name)} {home_score:.1f} - {away_score:.1f} {clean_team_name(away_team.team_name)} \n" 
            for week, home_score, away_score in previous_matchups],
            
            f"\n#### Playoff Picture",
            f"**{clean_team_name(home_team.team_name)}:** {home_playoff_odds:.1f}% chance \n",
            f"**{clean_team_name(away_team.team_name)}:**{away_playoff_odds:.1f}% chance\n"
        ])
        
        markdown_content.append("\n---\n")  # Add separator between matchups

    markdown_filename = f"{datetime.now().strftime('%Y-%m-%d')}-Week-{week+1}_preview.md"
    os.makedirs(f"../_posts", exist_ok=True)
    with open(f"../_posts/{markdown_filename}", 'w') as f:
        f.write('\n'.join(markdown_content))
        
        
def generate_advanced_analytics_page(league, teams, box_scores, week):
    # First generate all the JSON files we'll need
    generate_analytics_json(league, teams, week, box_scores)
    opt_chart_data = f"../assets/json/analytics/optimization_chart.json"
    with open(opt_chart_data, "r") as json_file:
        opt_chart= json_file.read()
    # Ensure JSON is properly formatted
    parsed_opt_chart = json.loads(opt_chart)
    formatted_opt_chart = json.dumps(parsed_opt_chart, indent=4) 
    
    sch_chart_data = f"../assets/json/analytics/schedule_chart.json"
    with open(sch_chart_data, "r") as json_file:
        sch_chart= json_file.read()
    # Ensure JSON is properly formatted
    parsed_sch_chart = json.loads(sch_chart)
    formatted_sch_chart = json.dumps(parsed_sch_chart, indent=4) 
    
    
    pos_chart_data = f"../assets/json/analytics/position_chart.json"
    with open(pos_chart_data, "r") as json_file:
        pos_chart= json_file.read()
    # Ensure JSON is properly formatted
    parsed_pos_chart = json.loads(pos_chart)
    formatted_pos_chart = json.dumps(parsed_pos_chart, indent=4) 
    content = [
        "---",
        "layout: page",
        "permalink: /analytics/",
        "title: advanced analytics",
        "nav: true",
        "nav_order: 6",
        "description: Advanced team and league analytics",
        "chart:",
        "  echarts: true",
        "pretty_table: True",
        "---",
        "\n## Advanced Analytics\n",
        "<br>",
        "\n### Lineup Efficiency Over Time\n",
        '```echarts',
        formatted_opt_chart,
        '```\n',
        
        "<br>",
        "\n### Positional Advantages\n",
        '```echarts',
        formatted_pos_chart,
        '```\n',
    ]
    
    os.makedirs("../_pages", exist_ok=True)
    with open(f"../_pages/analytics.md", 'w') as f:
        f.write('\n'.join(content))