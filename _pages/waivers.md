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

<style>
  table[data-toggle="table"] tbody td {
    color: #2c3e50 !important;
  }
</style>
### Best Pickups
<table
data-click-to-select="true"
data-search="false"
data-toggle="table"
data-url="{{ "/assets/json/transactions/best_fa_2025.json"}}">
<thead>
    <tr>
    <th data-field="player_name" data-halign="left" data-align="left" data-sortable="false">Player</th>
     <th data-field="team" data-halign="center" data-align="center" data-sortable="false">Team</th>
     <th data-field="position" data-halign="center" data-align="center" data-sortable="false">Pos</th>
     <th data-field="week" data-halign="center" data-align="center" data-sortable="false">Week</th>
     <th data-field="total_points" data-halign="center" data-align="center" data-sortable="true">Total Pts</th>
     <th data-field="avg_per_week" data-halign="center" data-align="center" data-sortable="true">PPG</th>
     <th data-field="points_above_prev" data-halign="center" data-align="center" data-sortable="true">+/- Prev Avg</th>
     <th data-field="weeks_played" data-halign="center" data-align="center" data-sortable="false">Weeks</th>
     <th data-field="type" data-halign="center" data-align="center" data-sortable="true">Type</th>
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
data-url="{{ "/assets/json/transactions/all_fa_2025.json"}}">
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
