---
layout: page
title: pink pony club (2024)
description: manager(s) - connor dickson and monika monko
img: assets/img/PONY_2024.jpg
importance: 3
category: archive-2024
related_publications: false
chart:
  echarts: true
pretty_table: True
---

### <center> 2024 Season Final Stats </center>

#### Summary
<table
data-click-to-select="true"
data-search="false"
data-toggle="table"
data-url="{{ "/assets/json/archive/2024/PONY_2024_summary.json" }}">
<thead>
    <tr>
        <th data-field="category" data-halign="left" data-align="left" data-sortable="false">Category</th>
        <th data-field="value" data-halign="center" data-align="center" data-sortable="false">Value</th>
    </tr>
</thead>
</table>

<br><br>

```echarts
{
    "tooltip": {
        "trigger": "axis"
    },
    "legend": {
        "data": [
            "Points For",
            "Points Against",
            "League Avg"
        ]
    },
    "grid": {
        "top": "10%",
        "bottom": "5%",
        "left": "6%",
        "right": "0%"
    },
    "xAxis": {
        "type": "category",
        "data": [
            "Week 1",
            "Week 2",
            "Week 3",
            "Week 4",
            "Week 5",
            "Week 6",
            "Week 7",
            "Week 8",
            "Week 9",
            "Week 10",
            "Week 11",
            "Week 12",
            "Week 13"
        ]
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
        }
    },
    "series": [
        {
            "name": "Points For",
            "type": "line",
            "data": [
                131.9,
                125.0,
                137.3,
                155.2,
                130.0,
                137.9,
                113.6,
                167.1,
                141.0,
                129.2,
                100.0,
                137.0,
                155.5
            ],
            "symbol": "circle",
            "symbolSize": 8,
            "lineStyle": {
                "width": 3
            }
        },
        {
            "name": "Points Against",
            "type": "line",
            "data": [
                98.6,
                99.9,
                160.0,
                132.5,
                142.4,
                115.6,
                112.0,
                161.6,
                136.1,
                154.8,
                98.5,
                119.4,
                106.0
            ],
            "symbol": "circle",
            "symbolSize": 8,
            "lineStyle": {
                "width": 3
            }
        },
        {
            "name": "League Avg",
            "type": "line",
            "data": [
                118.3,
                119.0,
                125.4,
                122.1,
                131.4,
                123.6,
                111.5,
                137.3,
                134.8,
                115.0,
                128.4,
                119.8,
                132.6,
                252.9
            ],
            "symbol": "none",
            "lineStyle": {
                "type": "dashed",
                "width": 2
            }
        }
    ]
}
```
<br><br>

#### Final Roster
<table
 data-click-to-select="true"
 data-search="false"
 data-toggle="table"
 data-url="{{ "/assets/json/team_rosters/PONY_2024.json"}}">
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
data-search="false"
data-toggle="table"
data-url="{{ "/assets/json/archive/2024/PONY_2024_positions.json" }}">
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
{
    "tooltip": {
        "trigger": "item",
        "formatter": "{a} <br/>{b}: {d}%"
    },
    "legend": {
        "orient": "vertical",
        "left": "left",
        "data": [
            "QB",
            "RB",
            "WR",
            "TE",
            "D/ST",
            "K"
        ]
    },
    "series": [
        {
            "name": "Position Points",
            "type": "pie",
            "radius": [
                "50%",
                "70%"
            ],
            "avoidLabelOverlap": false,
            "data": [
                {
                    "value": 42.1,
                    "name": "QB"
                },
                {
                    "value": 53.5,
                    "name": "RB"
                },
                {
                    "value": 41.3,
                    "name": "WR"
                },
                {
                    "value": 6.1,
                    "name": "TE"
                }
            ]
        }
    ]
}
```

#### Lineup Efficiency
<table
    data-click-to-select="true"
    data-search="false"
    data-toggle="table"
    data-url="{{ "/assets/json/archive/2024/PONY_2024_weekly_eff.json" }}">
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
    data-search="false"
    data-toggle="table"
    data-url="{{ "/assets/json/archive/2024/PONY_2024_draft.json" }}">
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
    data-search="false"
    data-toggle="table"
    data-url="{{ "/assets/json/archive/2024/PONY_2024_h2h.json" }}">
    <thead>
        <tr>
            <th data-field="opponent" data-halign="left" data-align="left" data-sortable="false">Opponent</th>
            <th data-field="record" data-halign="center" data-align="center" data-sortable="true">Record</th>
            <th data-field="points" data-halign="center" data-align="center" data-sortable="false">Avg Score</th>
        </tr>
    </thead>
</table>
