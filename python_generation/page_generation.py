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
layout: about
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

## Welcome to the site for the Family Fantasy Footbal League! We are currently in the 2024-25 season. This site is clearly still under development

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
    weekly_scoring_chart = f"../assets/json/team_data/{team.team_abbrev}_{league.year}_weekly_scores.json"
    with open(weekly_scoring_chart, "r") as json_file:
        weekly_scores = json_file.read()
    # Ensure JSON is properly formatted
    parsed_weekly_scores = json.loads(weekly_scores)
    formatted_weekly_scores = json.dumps(parsed_weekly_scores, indent=4) 
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
        
        
def generate_team_weekly_recap(league: League, team_name: str,box_scores, news_data: Dict, output_dir: str = "_posts"):
    # First find the team
    team = next((t for t in league.teams if clean_team_name(t.team_name) == team_name), None)
    if not team:
        raise ValueError(f"Team {team_name} not found")
    team_abbrev = team.team_abbrev    
    # Create markdown content
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    markdown_content = [
        "---",
        "layout: post",
        f"title: {team_name} Week {league.current_week-1} Report",
        f"date: {current_date}",
        "description: Weekly team status report",
        f"tags: 2024-25, WeeklyRecap, Week{league.current_week - 1}",
        "categories: team-reports",
        "tabs: true",
        "pretty_table: = true",
        "---",
    ]
    # After frontmatter but before injury report, add:
    box = next((b for b in box_scores[league.current_week - 1] if b.home_team == team or b.away_team == team), None)
    standings = league.standings()
    current_rank = next((i for i, t in enumerate(standings, 1) if t.team_id == team.team_id), None)
    
    
    if box:
        opponent = box.home_team if box.away_team == team else box.away_team
        team_score = box.home_score if box.home_team == team else box.away_score
        opp_score = box.away_score if box.home_team == team else box.home_score
        result = "Won" if (box.home_team == team and team_score > opp_score) or \
                         (box.away_team == team and team_score > opp_score) else "Lost"
        
      # After getting box score but before adding to markdown_content
    weekly_effs, _, total_optimal_points, total_actual_points = get_efficiencies(league.current_week-1, box_scores, team)
    efficiency = (total_actual_points/total_optimal_points * 100) if total_optimal_points > 0 else 0
    
    # Get highest scoring player
    if box:
        lineup = box.home_lineup if box.home_team == team else box.away_lineup
        best_player = max(lineup, key=lambda x: x.points if x.slot_position != 'BE' else 0)
        
    # Get worst benching for this week
    worst_benchings = get_benchings(league.current_week-1, box_scores, [team])
    week_benchings = [b for b in worst_benchings.values() 
                     if b['week'] == league.current_week and 
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
                        f"**Details:** {news.get('longComment', '')}",
                    ])
    
    # Generate roster data for JSON
    roster_data = []
    optimal_data = []
    
    box = next((b for b in box_scores[league.current_week - 1] if b.home_team == team or b.away_team == team), None)
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
    nfl_week = league.current_week -1
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
        
def generate_league_weekly_recap_markdown(league: League, box_scores):
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nfl_week = league.nfl_week
    nfl_year = league.year
    
    markdown_content = [
        "---",
        "layout: post",
        f"title: Week {nfl_week-1} League Recap",
        f"date: {current_date}",
        "description: Weekly league recap and standings",
        f"tags: 2024-25, WeeklyRecap, Week{league.current_week - 1}",
        "categories: league-recaps",
        "tabs: true",
        "pretty_table: true",
        "---",
        "\n## Weekly Matchups\n"
    ]
    
    # Get box scores and standings
    
    standings = league.standings()
    
    # Process each matchup
    for box in box_scores[nfl_week-1]:
        if not box.away_team:  # Skip bye weeks
            continue
            
        # Get matchup scores
        home_score = box.home_score
        away_score = box.away_score
        
        # Get highest scoring player in matchup
        all_players = box.home_lineup + box.away_lineup
        best_player = max(all_players, key=lambda x: x.points if x.slot_position != 'BE' else 0)
        best_player_team = box.home_team if best_player in box.home_lineup else box.away_team
        
        # Get worst benchings for both teams
        worst_benchings = get_benchings(nfl_week, box_scores, [box.home_team, box.away_team])
        matchup_benchings = [b for b in worst_benchings.values() 
                           if b['week'] == nfl_week and 
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

    # Save standings JSON
    standings_filename = f"Week_{nfl_week-1}_{nfl_year}_standings.json"
    os.makedirs(f"../assets/json/standings", exist_ok=True)
    with open(f"../assets/json/standings/{standings_filename}", 'w') as f:
        json.dump(standings_data, f, indent=2)

    # Replace the markdown standings table with bootstrap table
    markdown_content.extend([
        "## Current Standings\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"575\"",
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

    # Save markdown file
    markdown_filename = f"{datetime.now().strftime('%Y-%m-%d')}-Week-{nfl_week-1}_Recap.md"
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
        

def generate_players_page(league: League):
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
                scaled_projection = player.projected_total_points / 17 * league.current_week

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
        "nav: true",
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
        "Below are the top 10 performers at each position through Week " + str(league.current_week) + ".\n\n"
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
        "layout: page",
        "permalink: /records/",
        "title: records",
        "nav: false",
        "nav_order: 7",
        "description: All-time league records and notable achievements",
        "chart:",
        "echarts: true",
        "pretty_table: True",
        "---",
        "\n# League Records\n",
        
        "\n## All-Time Records\n",
        f"Updated through {datetime.now().strftime('%Y')}\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"285\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        "data-url=\"{{ \"/assets/json/records/all_time_records.json\" }}\">",
        "<thead>",
        "<tr>",
        "<th data-field=\"category\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\">Record</th>",
        "<th data-field=\"value\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Value</th>",
        "<th data-field=\"team\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\">Team</th>",
        "<th data-field=\"year\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Year</th>",
        "</tr>",
        "</thead>",
        "</table><br>\n",
        
        "\n## Season Records\n",
        f"Records from individual seasons\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"165\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        "data-url=\"{{ \"/assets/json/records/season_records.json\" }}\">",
        "<thead>",
        "<tr>",
        "<th data-field=\"category\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\">Record</th>",
        "<th data-field=\"value\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Value</th>",
        "<th data-field=\"team\" data-halign=\"left\" data-align=\"left\" data-sortable=\"true\">Team</th>",
        "<th data-field=\"year\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Year</th>",
        "</tr>",
        "</thead>",
        "</table><br>\n",
        
        "\n## Game Records\n",
        f"Single game achievements\n",
        "<table",
        "data-click-to-select=\"true\"",
        "data-height=\"165\"",
        "data-search=\"false\"",
        "data-toggle=\"table\"",
        "data-url=\"{{ \"/assets/json/records/game_records.json\" }}\">",
        "<thead>",
        "<tr>",
        "<th data-field=\"category\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\">Record</th>",
        "<th data-field=\"value\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Value</th>",
        "<th data-field=\"details\" data-halign=\"left\" data-align=\"left\" data-sortable=\"false\">Details</th>",
        "<th data-field=\"year\" data-halign=\"center\" data-align=\"center\" data-sortable=\"true\">Year</th>",
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