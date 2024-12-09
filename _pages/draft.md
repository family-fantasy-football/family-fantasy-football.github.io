---
layout: page
permalink: /draft/
title: draft
nav: true
nav_order: 4
description: This page will do draft analysis, and be updated throughout the season
chart:
  echarts: true
pretty_table: True
---

Still need to add the top 5 and worst 5 picks, as well as make this page automated


<table
    data-click-to-select="true"
    data-height="800"
    data-search="false"
    data-toggle="table"
    data-url="{{ "/assets/json/team_data/draft_total_2024.json" }}">
    <thead>
        <tr>
            <th data-field="team" data-halign="center" data-align="left" data-sortable="true">Team</th>
            <th data-field="round" data-halign="center" data-align="center" data-sortable="true">Round</th>
            <th data-field="pick" data-halign="center" data-align="center" data-sortable="false">Pick</th>
            <th data-field="draft_position" data-halign="center" data-align="center" data-sortable="true">Overall</th>
            <th data-field="player_name" data-halign="left" data-align="left" data-sortable="false">Player</th>
            <th data-field="grade" data-halign="center" data-align="center" data-sortable="true">Grade</th>
        </tr>
    </thead>
</table>