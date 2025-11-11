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

<style>
  table[data-toggle="table"] tbody td {
    color: #2c3e50 !important;
  }
</style>

### All Trades
<table
data-click-to-select="true"
data-search="false"
data-toggle="table"
data-url="{{ "/assets/json/transactions/trades_2025.json"}}">
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
{
    "title": {
        "text": "Trade Network",
        "left": "center",
        "top": "5%",
        "textStyle": {
            "fontSize": 20
        },
        "show": false
    },
    "series": [
        {
            "type": "graph",
            "layout": "circular",
            "symbolSize": 50,
            "roam": true,
            "label": {
                "show": true
            },
            "edgeSymbol": [
                "circle",
                "arrow"
            ],
            "edgeSymbolSize": [
                4,
                10
            ],
            "data": [
                {
                    "id": "Third Time's the Charm?",
                    "name": "Third Time's the Charm?",
                    "itemStyle": {
                        "color": "hsl(0.0, 70%, 50%)"
                    }
                },
                {
                    "id": "90s MonCon",
                    "name": "90s MonCon",
                    "itemStyle": {
                        "color": "hsl(32.72727272727273, 70%, 50%)"
                    }
                },
                {
                    "id": "Rookie Mistake",
                    "name": "Rookie Mistake",
                    "itemStyle": {
                        "color": "hsl(65.45454545454545, 70%, 50%)"
                    }
                },
                {
                    "id": "Americas Team",
                    "name": "Americas Team",
                    "itemStyle": {
                        "color": "hsl(98.18181818181819, 70%, 50%)"
                    }
                },
                {
                    "id": "Michael's Managable Team",
                    "name": "Michael's Managable Team",
                    "itemStyle": {
                        "color": "hsl(130.9090909090909, 70%, 50%)"
                    }
                },
                {
                    "id": "To Infinity and Bijan!",
                    "name": "To Infinity and Bijan!",
                    "itemStyle": {
                        "color": "hsl(163.63636363636363, 70%, 50%)"
                    }
                },
                {
                    "id": "Mcconky Donkeys",
                    "name": "Mcconky Donkeys",
                    "itemStyle": {
                        "color": "hsl(196.36363636363637, 70%, 50%)"
                    }
                },
                {
                    "id": "Mama Daughter Duo",
                    "name": "Mama Daughter Duo",
                    "itemStyle": {
                        "color": "hsl(229.0909090909091, 70%, 50%)"
                    }
                },
                {
                    "id": "Abbey's TNT Team",
                    "name": "Abbey's TNT Team",
                    "itemStyle": {
                        "color": "hsl(261.8181818181818, 70%, 50%)"
                    }
                },
                {
                    "id": "Game of Zones - House Hamlin",
                    "name": "Game of Zones - House Hamlin",
                    "itemStyle": {
                        "color": "hsl(294.54545454545456, 70%, 50%)"
                    }
                },
                {
                    "id": "Emma's Excellent Team",
                    "name": "Emma's Excellent Team",
                    "itemStyle": {
                        "color": "hsl(327.27272727272725, 70%, 50%)"
                    }
                },
                {
                    "id": "Big Titi Energy",
                    "name": "Big Titi Energy",
                    "itemStyle": {
                        "color": "hsl(360.0, 70%, 50%)"
                    }
                }
            ],
            "links": [
                {
                    "source": "Third Time's the Charm?",
                    "target": "To Infinity and Bijan!",
                    "value": 1,
                    "tooltip": {
                        "show": true
                    },
                    "name": "Third Time's the Charm?: Chris Godwin Jr. \u27f7 To Infinity and Bijan!: TreVeyon Henderson"
                },
                {
                    "source": "Michael's Managable Team",
                    "target": "Third Time's the Charm?",
                    "value": 1,
                    "tooltip": {
                        "show": true
                    },
                    "name": "Michael's Managable Team: RJ Harvey \u27f7 Third Time's the Charm?: Harold Fannin Jr."
                },
                {
                    "source": "Emma's Excellent Team",
                    "target": "Third Time's the Charm?",
                    "value": 1,
                    "tooltip": {
                        "show": true
                    },
                    "name": "Emma's Excellent Team: Dak Prescott, Tyrone Tracy Jr. \u27f7 Third Time's the Charm?: Trevor Lawrence, Zach Ertz, Aaron Jones Sr."
                }
            ],
            "lineStyle": {
                "opacity": 0.9,
                "width": 2,
                "curveness": 0
            }
        }
    ],
    "grid": {
        "top": "15%"
    }
}
```

