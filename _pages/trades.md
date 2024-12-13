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
data-url="{{ "/assets/json/transactions/trades_2024.json"}}">
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
                    "id": "Who Killed Charbonnet Ramsey?",
                    "name": "Who Killed Charbonnet Ramsey?",
                    "itemStyle": {
                        "color": "hsl(0.0, 70%, 50%)"
                    }
                },
                {
                    "id": "Pink Pony Club",
                    "name": "Pink Pony Club",
                    "itemStyle": {
                        "color": "hsl(40.0, 70%, 50%)"
                    }
                },
                {
                    "id": "Tom and Jerry",
                    "name": "Tom and Jerry",
                    "itemStyle": {
                        "color": "hsl(80.0, 70%, 50%)"
                    }
                },
                {
                    "id": "Hit and Ruggs",
                    "name": "Hit and Ruggs",
                    "itemStyle": {
                        "color": "hsl(120.0, 70%, 50%)"
                    }
                },
                {
                    "id": "Michael's Managable Team",
                    "name": "Michael's Managable Team",
                    "itemStyle": {
                        "color": "hsl(160.0, 70%, 50%)"
                    }
                },
                {
                    "id": "To Infinity and Bijan!",
                    "name": "To Infinity and Bijan!",
                    "itemStyle": {
                        "color": "hsl(200.0, 70%, 50%)"
                    }
                },
                {
                    "id": "Fantasy Guru Kayden",
                    "name": "Fantasy Guru Kayden",
                    "itemStyle": {
                        "color": "hsl(240.0, 70%, 50%)"
                    }
                },
                {
                    "id": "Mama Daughter Duo",
                    "name": "Mama Daughter Duo",
                    "itemStyle": {
                        "color": "hsl(280.0, 70%, 50%)"
                    }
                },
                {
                    "id": "Abbey Road to Victory",
                    "name": "Abbey Road to Victory",
                    "itemStyle": {
                        "color": "hsl(320.0, 70%, 50%)"
                    }
                },
                {
                    "id": "Hamlin My Business ",
                    "name": "Hamlin My Business ",
                    "itemStyle": {
                        "color": "hsl(360.0, 70%, 50%)"
                    }
                }
            ],
            "links": [
                {
                    "source": "Pink Pony Club",
                    "target": "To Infinity and Bijan!",
                    "value": 1,
                    "tooltip": {
                        "show": true
                    },
                    "name": "Pink Pony Club: Mike Gesicki, Russell Wilson \u27f7 To Infinity and Bijan!: Cade Otton, Jameis Winston"
                },
                {
                    "source": "Pink Pony Club",
                    "target": "Tom and Jerry",
                    "value": 1,
                    "tooltip": {
                        "show": true
                    },
                    "name": "Pink Pony Club: Jake Ferguson, Tank Dell \u27f7 Tom and Jerry: Evan Engram, Jalen Coker"
                },
                {
                    "source": "Hamlin My Business ",
                    "target": "Michael's Managable Team",
                    "value": 1,
                    "tooltip": {
                        "show": true
                    },
                    "name": "Hamlin My Business : Justin Herbert \u27f7 Michael's Managable Team: Aaron Jones"
                },
                {
                    "source": "Michael's Managable Team",
                    "target": "Who Killed Charbonnet Ramsey?",
                    "value": 1,
                    "tooltip": {
                        "show": true
                    },
                    "name": "Michael's Managable Team: Brock Bowers, Amari Cooper \u27f7 Who Killed Charbonnet Ramsey?: DeMario Douglas, Zack Moss, Drake Maye"
                },
                {
                    "source": "Hamlin My Business ",
                    "target": "Who Killed Charbonnet Ramsey?",
                    "value": 1,
                    "tooltip": {
                        "show": true
                    },
                    "name": "Hamlin My Business : Javonte Williams \u27f7 Who Killed Charbonnet Ramsey?: Romeo Doubs"
                },
                {
                    "source": "Abbey Road to Victory",
                    "target": "Pink Pony Club",
                    "value": 1,
                    "tooltip": {
                        "show": true
                    },
                    "name": "Abbey Road to Victory: Nico Collins \u27f7 Pink Pony Club: DeVonta Smith"
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

