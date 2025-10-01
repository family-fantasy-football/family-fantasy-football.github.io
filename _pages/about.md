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

## Welcome to the site for the Family Fantasy Footbal League! We are currently in the 2025-26 season.

<div style="margin-bottom: 30px;">

</div>


The current top scorer is: Connor Dickson and Monika Monko (555.29)

The current bottom scorer is: Christine Hamlin (314.47)

Highest Scoring Week: Kyle Hamlin - 176.38 points (Week 1)

Lowest Scoring Week: Emma Grau - 67.94 points (Week 2)

Luckiest Team: Kayden Mullins (1.1) Wins Above Expected

Unluckiest Team: Ryan Ratcliff (-1.1) Wins Below Expected




### Current Standings:

<table
    data-click-to-select="true"
    data-pagination="false"
    data-search="false"
    data-toggle="table"
    data-url="{{ "/assets/json/standings.json"}}">
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
{
    "title": {
        "text": "Standings Over Time",
        "left": "center"
    },
    "tooltip": {
        "trigger": "item",
        "formatter": "{a}<br/>Week {b}: Rank {c}"
    },
    "xAxis": {
        "type": "category",
        "name": "Week",
        "nameLocation": "middle",
        "nameGap": 30,
        "data": [
            1,
            2,
            3,
            4
        ]
    },
    "yAxis": {
        "type": "value",
        "name": "Rank",
        "nameLocation": "middle",
        "nameGap": 20,
        "inverse": true,
        "min": 1,
        "max": 12
    },
    "series": [
        {
            "name": "90s MonCon",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#1f77b4"
            },
            "itemStyle": {
                "color": "#1f77b4"
            },
            "data": [
                7,
                4,
                3,
                1
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "90s MonCon"
            }
        },
        {
            "name": "Abbey's TNT Team ",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#98df8a"
            },
            "itemStyle": {
                "color": "#98df8a"
            },
            "data": [
                4,
                8,
                5,
                4
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Abbey's TNT ..."
            }
        },
        {
            "name": "Americas Team ",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#c7c7c7"
            },
            "itemStyle": {
                "color": "#c7c7c7"
            },
            "data": [
                12,
                10,
                10,
                10
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Americas Team "
            }
        },
        {
            "name": "Big Titi Energy",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#17becf"
            },
            "itemStyle": {
                "color": "#17becf"
            },
            "data": [
                11,
                12,
                12,
                12
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Big Titi Ene..."
            }
        },
        {
            "name": "Emma's Excellent Team",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#bcbd22"
            },
            "itemStyle": {
                "color": "#bcbd22"
            },
            "data": [
                8,
                11,
                11,
                11
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Emma's Excel..."
            }
        },
        {
            "name": "Game of Zones - House Hamlin",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#aec7e8"
            },
            "itemStyle": {
                "color": "#aec7e8"
            },
            "data": [
                1,
                1,
                1,
                2
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Game of Zone..."
            }
        },
        {
            "name": "Mama Daughter Duo",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#9467bd"
            },
            "itemStyle": {
                "color": "#9467bd"
            },
            "data": [
                3,
                5,
                4,
                6
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Mama Daughte..."
            }
        },
        {
            "name": "Mcconky Donkeys",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#f7b6d2"
            },
            "itemStyle": {
                "color": "#f7b6d2"
            },
            "data": [
                10,
                9,
                7,
                9
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Mcconky Donk..."
            }
        },
        {
            "name": "Michael's Managable Team",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#ffbb78"
            },
            "itemStyle": {
                "color": "#ffbb78"
            },
            "data": [
                5,
                2,
                2,
                3
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Michael's Ma..."
            }
        },
        {
            "name": "Rookie Mistake",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#8c564b"
            },
            "itemStyle": {
                "color": "#8c564b"
            },
            "data": [
                9,
                7,
                9,
                7
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Rookie Mistake"
            }
        },
        {
            "name": "Third Time's the Charm?",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#d62728"
            },
            "itemStyle": {
                "color": "#d62728"
            },
            "data": [
                6,
                3,
                6,
                5
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Third Time's..."
            }
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#c49c94"
            },
            "itemStyle": {
                "color": "#c49c94"
            },
            "data": [
                2,
                6,
                8,
                8
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "To Infinity ..."
            }
        }
    ],
    "grid": {
        "left": "1%",
        "right": "0%",
        "bottom": "1%",
        "top": "10%",
        "containLabel": true
    }
}
```
<br><br>

```echarts
{
    "title": {
        "text": "Points For vs Points Against",
        "left": "center"
    },
    "tooltip": {
        "trigger": "item",
        "formatter": "{b}"
    },
    "xAxis": {
        "type": "value",
        "name": "Points For",
        "nameLocation": "middle",
        "nameGap": 30,
        "min": 164.0,
        "max": 712.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": 164.0,
        "max": 712.0
    },
    "series": [
        {
            "name": "Teams",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                {
                    "name": "Third Time's the Charm?",
                    "value": [
                        460.17,
                        386.12
                    ]
                },
                {
                    "name": "90s MonCon",
                    "value": [
                        555.29,
                        425.91
                    ]
                },
                {
                    "name": "Rookie Mistake",
                    "value": [
                        479.61,
                        450.9
                    ]
                },
                {
                    "name": "Americas Team ",
                    "value": [
                        484.86,
                        502.97
                    ]
                },
                {
                    "name": "Michael's Managable Team",
                    "value": [
                        538.54,
                        476.52
                    ]
                },
                {
                    "name": "To Infinity and Bijan!",
                    "value": [
                        461.65,
                        507.51
                    ]
                },
                {
                    "name": "Mcconky Donkeys",
                    "value": [
                        375.84,
                        403.24
                    ]
                },
                {
                    "name": "Mama Daughter Duo",
                    "value": [
                        533.49,
                        526.86
                    ]
                },
                {
                    "name": "Abbey's TNT Team ",
                    "value": [
                        506.56,
                        459.37
                    ]
                },
                {
                    "name": "Game of Zones - House Hamlin",
                    "value": [
                        546.31,
                        424.52
                    ]
                },
                {
                    "name": "Emma's Excellent Team",
                    "value": [
                        355.83,
                        486.92
                    ]
                },
                {
                    "name": "Big Titi Energy",
                    "value": [
                        314.47,
                        561.78
                    ]
                }
            ],
            "label": {
                "show": true,
                "position": "top",
                "formatter": "{b}"
            }
        },
        {
            "name": "Diagonal",
            "type": "line",
            "lineStyle": {
                "type": "dashed",
                "color": "gray"
            },
            "showSymbol": false,
            "data": [
                [
                    164.0,
                    164.0
                ],
                [
                    712.0,
                    712.0
                ]
            ]
        },
        {
            "name": "Average Lines",
            "type": "line",
            "markLine": {
                "silent": true,
                "data": [
                    {
                        "xAxis": 467.72,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 467.72,
                        "lineStyle": {
                            "color": "red",
                            "opacity": 0.5
                        }
                    }
                ]
            }
        }
    ],
    "grid": {
        "left": "0%",
        "right": "5%",
        "bottom": "10%",
        "top": "10%",
        "containLabel": true
    }
}
```
<br><br>

```echarts
{
    "title": {
        "text": "Weekly Score Distribution by Team",
        "left": "center"
    },
    "xAxis": {
        "type": "category",
        "name": "Teams",
        "nameLocation": "middle",
        "nameGap": 30,
        "data": [
            "90s",
            "HMB",
            "MMT",
            "ARV",
            "TTC",
            "JST",
            "TOM",
            "TIB",
            "KTT",
            "RRT",
            "EET",
            "BTE"
        ]
    },
    "yAxis": {
        "type": "value",
        "name": "Points Scored",
        "nameLocation": "middle",
        "nameGap": 30
    },
    "series": [
        {
            "name": "Weekly Scores",
            "type": "boxplot",
            "data": [
                [
                    0.0,
                    0.0,
                    0.0,
                    83.6,
                    170.76
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    86.2,
                    176.38
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    83.96,
                    148.67
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    84.82,
                    157.57
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    63.97,
                    156.86
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    92.8,
                    157.16
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    70.9,
                    156.21
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    58.94,
                    137.55
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    65.07,
                    101.15
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    60.08,
                    148.62
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    50.96,
                    108.2
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    51.82,
                    82.52
                ]
            ],
            "itemStyle": {
                "borderWidth": 2
            }
        },
        {
            "name": "All Scores",
            "type": "scatter",
            "data": [
                [
                    0,
                    111.47,
                    "90s"
                ],
                [
                    0,
                    157.15,
                    "90s"
                ],
                [
                    0,
                    170.76,
                    "90s"
                ],
                [
                    0,
                    115.91,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    0,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    176.38,
                    "HMB"
                ],
                [
                    1,
                    119.75,
                    "HMB"
                ],
                [
                    1,
                    114.94,
                    "HMB"
                ],
                [
                    1,
                    135.24,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    2,
                    111.95,
                    "MMT"
                ],
                [
                    2,
                    141.03,
                    "MMT"
                ],
                [
                    2,
                    148.67,
                    "MMT"
                ],
                [
                    2,
                    136.89,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    0.0,
                    "MMT"
                ],
                [
                    3,
                    115.72,
                    "ARV"
                ],
                [
                    3,
                    113.09,
                    "ARV"
                ],
                [
                    3,
                    120.18,
                    "ARV"
                ],
                [
                    3,
                    157.57,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    3,
                    0.0,
                    "ARV"
                ],
                [
                    4,
                    106.14,
                    "TTC"
                ],
                [
                    4,
                    111.87,
                    "TTC"
                ],
                [
                    4,
                    85.3,
                    "TTC"
                ],
                [
                    4,
                    156.86,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    4,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    126.38,
                    "JST"
                ],
                [
                    5,
                    126.22,
                    "JST"
                ],
                [
                    5,
                    157.16,
                    "JST"
                ],
                [
                    5,
                    123.73,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    0.0,
                    "JST"
                ],
                [
                    6,
                    103.67,
                    "TOM"
                ],
                [
                    6,
                    125.2,
                    "TOM"
                ],
                [
                    6,
                    94.53,
                    "TOM"
                ],
                [
                    6,
                    156.21,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    6,
                    0.0,
                    "TOM"
                ],
                [
                    7,
                    134.09,
                    "TIB"
                ],
                [
                    7,
                    111.43,
                    "TIB"
                ],
                [
                    7,
                    78.58,
                    "TIB"
                ],
                [
                    7,
                    137.55,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    7,
                    0.0,
                    "TIB"
                ],
                [
                    8,
                    101.15,
                    "KTT"
                ],
                [
                    8,
                    99.4,
                    "KTT"
                ],
                [
                    8,
                    88.53,
                    "KTT"
                ],
                [
                    8,
                    86.76,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    8,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    80.1,
                    "RRT"
                ],
                [
                    9,
                    148.62,
                    "RRT"
                ],
                [
                    9,
                    144.61,
                    "RRT"
                ],
                [
                    9,
                    111.53,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    9,
                    0.0,
                    "RRT"
                ],
                [
                    10,
                    108.2,
                    "EET"
                ],
                [
                    10,
                    67.94,
                    "EET"
                ],
                [
                    10,
                    73.63,
                    "EET"
                ],
                [
                    10,
                    106.06,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    10,
                    0.0,
                    "EET"
                ],
                [
                    11,
                    81.59,
                    "BTE"
                ],
                [
                    11,
                    69.1,
                    "BTE"
                ],
                [
                    11,
                    81.26,
                    "BTE"
                ],
                [
                    11,
                    82.52,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    0.0,
                    "BTE"
                ]
            ]
        }
    ],
    "grid": {
        "left": "4%",
        "right": "1%",
        "bottom": "1%",
        "top": "10%",
        "containLabel": true
    }
}
```
<br><br>

### Average Position Rankings
```echarts
{
    "grid": {
        "top": "10%",
        "bottom": "15%",
        "left": "5%",
        "right": "0%",
        "containLabel": true
    },
    "xAxis": {
        "type": "category",
        "data": [
            "QB",
            "RB",
            "TE",
            "WR"
        ],
        "name": "Position",
        "nameLocation": "center",
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "yAxis": {
        "type": "category",
        "data": [
            "90s",
            "HMB",
            "MMT",
            "ARV",
            "TTC",
            "JST",
            "TOM",
            "TIB",
            "KTT",
            "RRT",
            "EET",
            "BTE"
        ],
        "name": "",
        "nameLocation": "end",
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "visualMap": {
        "min": 1,
        "max": 12,
        "calculable": true,
        "orient": "vertical",
        "show": false,
        "right": "right",
        "bottom": "30%",
        "text": [],
        "inRange": {
            "color": [
                "#4575b4",
                "#91bfdb",
                "#fee090",
                "#fc8d59",
                "#d73027"
            ]
        }
    },
    "series": [
        {
            "type": "heatmap",
            "data": [
                [
                    0,
                    0,
                    4
                ],
                [
                    1,
                    0,
                    1
                ],
                [
                    2,
                    0,
                    4
                ],
                [
                    3,
                    0,
                    6
                ],
                [
                    0,
                    1,
                    1
                ],
                [
                    1,
                    1,
                    10
                ],
                [
                    2,
                    1,
                    3
                ],
                [
                    3,
                    1,
                    1
                ],
                [
                    0,
                    2,
                    3
                ],
                [
                    1,
                    2,
                    7
                ],
                [
                    2,
                    2,
                    5
                ],
                [
                    3,
                    2,
                    3
                ],
                [
                    0,
                    3,
                    9
                ],
                [
                    1,
                    3,
                    2
                ],
                [
                    2,
                    3,
                    12
                ],
                [
                    3,
                    3,
                    2
                ],
                [
                    0,
                    4,
                    2
                ],
                [
                    1,
                    4,
                    8
                ],
                [
                    2,
                    4,
                    7
                ],
                [
                    3,
                    4,
                    10
                ],
                [
                    0,
                    5,
                    5
                ],
                [
                    1,
                    5,
                    3
                ],
                [
                    2,
                    5,
                    6
                ],
                [
                    3,
                    5,
                    4
                ],
                [
                    0,
                    6,
                    10
                ],
                [
                    1,
                    6,
                    4
                ],
                [
                    2,
                    6,
                    2
                ],
                [
                    3,
                    6,
                    9
                ],
                [
                    0,
                    7,
                    8
                ],
                [
                    1,
                    7,
                    5
                ],
                [
                    2,
                    7,
                    11
                ],
                [
                    3,
                    7,
                    5
                ],
                [
                    0,
                    8,
                    7
                ],
                [
                    1,
                    8,
                    9
                ],
                [
                    2,
                    8,
                    9
                ],
                [
                    3,
                    8,
                    11
                ],
                [
                    0,
                    9,
                    6
                ],
                [
                    1,
                    9,
                    6
                ],
                [
                    2,
                    9,
                    1
                ],
                [
                    3,
                    9,
                    8
                ],
                [
                    0,
                    10,
                    11
                ],
                [
                    1,
                    10,
                    11
                ],
                [
                    2,
                    10,
                    10
                ],
                [
                    3,
                    10,
                    7
                ],
                [
                    0,
                    11,
                    12
                ],
                [
                    1,
                    11,
                    12
                ],
                [
                    2,
                    11,
                    8
                ],
                [
                    3,
                    11,
                    12
                ]
            ],
            "label": {
                "show": true,
                "fontSize": 12
            }
        }
    ]
}
````


### Position Breakdowns By Week
<br><br>

##### QB
```echarts
{
    "grid": {
        "top": "10%",
        "bottom": "13%",
        "left": "5%",
        "right": "0%",
        "containLabel": true
    },
    "xAxis": {
        "type": "category",
        "data": [
            1,
            2,
            3,
            4
        ],
        "name": "Week",
        "nameLocation": "center",
        "nameGap": 35,
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "yAxis": {
        "type": "category",
        "data": [
            "EET",
            "BTE",
            "ARV",
            "90s",
            "RRT",
            "TOM",
            "JST",
            "HMB",
            "KTT",
            "TIB",
            "TTC",
            "MMT"
        ],
        "name": "",
        "nameLocation": "end",
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "visualMap": {
        "min": 1,
        "max": 12,
        "calculable": true,
        "orient": "vertical",
        "right": "right",
        "show": false,
        "bottom": "30%",
        "text": [],
        "inRange": {
            "color": [
                "#4575b4",
                "#91bfdb",
                "#fee090",
                "#fc8d59",
                "#d73027"
            ]
        }
    },
    "series": [
        {
            "type": "heatmap",
            "data": [
                [
                    0,
                    0,
                    11
                ],
                [
                    1,
                    0,
                    9
                ],
                [
                    2,
                    0,
                    12
                ],
                [
                    3,
                    0,
                    9
                ],
                [
                    0,
                    1,
                    2
                ],
                [
                    1,
                    1,
                    10
                ],
                [
                    2,
                    1,
                    10
                ],
                [
                    3,
                    1,
                    12
                ],
                [
                    0,
                    2,
                    6
                ],
                [
                    1,
                    2,
                    12
                ],
                [
                    2,
                    2,
                    2
                ],
                [
                    3,
                    2,
                    10
                ],
                [
                    0,
                    3,
                    12
                ],
                [
                    1,
                    3,
                    4
                ],
                [
                    2,
                    3,
                    8
                ],
                [
                    3,
                    3,
                    5
                ],
                [
                    0,
                    4,
                    10
                ],
                [
                    1,
                    4,
                    7
                ],
                [
                    2,
                    4,
                    4
                ],
                [
                    3,
                    4,
                    7
                ],
                [
                    0,
                    5,
                    7
                ],
                [
                    1,
                    5,
                    1
                ],
                [
                    2,
                    5,
                    11
                ],
                [
                    3,
                    5,
                    8
                ],
                [
                    0,
                    6,
                    3
                ],
                [
                    1,
                    6,
                    8
                ],
                [
                    2,
                    6,
                    1
                ],
                [
                    3,
                    6,
                    11
                ],
                [
                    0,
                    7,
                    5
                ],
                [
                    1,
                    7,
                    6
                ],
                [
                    2,
                    7,
                    9
                ],
                [
                    3,
                    7,
                    2
                ],
                [
                    0,
                    8,
                    4
                ],
                [
                    1,
                    8,
                    5
                ],
                [
                    2,
                    8,
                    7
                ],
                [
                    3,
                    8,
                    6
                ],
                [
                    0,
                    9,
                    1
                ],
                [
                    1,
                    9,
                    11
                ],
                [
                    2,
                    9,
                    6
                ],
                [
                    3,
                    9,
                    4
                ],
                [
                    0,
                    10,
                    9
                ],
                [
                    1,
                    10,
                    3
                ],
                [
                    2,
                    10,
                    5
                ],
                [
                    3,
                    10,
                    1
                ],
                [
                    0,
                    11,
                    8
                ],
                [
                    1,
                    11,
                    2
                ],
                [
                    2,
                    11,
                    3
                ],
                [
                    3,
                    11,
                    3
                ]
            ],
            "label": {
                "show": true,
                "fontSize": 12
            }
        }
    ]
}
```

##### RB
```echarts
{
    "grid": {
        "top": "10%",
        "bottom": "13%",
        "left": "5%",
        "right": "0%",
        "containLabel": true
    },
    "xAxis": {
        "type": "category",
        "data": [
            1,
            2,
            3,
            4
        ],
        "name": "Week",
        "nameLocation": "center",
        "nameGap": 35,
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "yAxis": {
        "type": "category",
        "data": [
            "EET",
            "BTE",
            "KTT",
            "HMB",
            "MMT",
            "TIB",
            "TOM",
            "JST",
            "ARV",
            "RRT",
            "TTC",
            "90s"
        ],
        "name": "",
        "nameLocation": "end",
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "visualMap": {
        "min": 1,
        "max": 12,
        "calculable": true,
        "orient": "vertical",
        "right": "right",
        "show": false,
        "bottom": "30%",
        "text": [],
        "inRange": {
            "color": [
                "#4575b4",
                "#91bfdb",
                "#fee090",
                "#fc8d59",
                "#d73027"
            ]
        }
    },
    "series": [
        {
            "type": "heatmap",
            "data": [
                [
                    0,
                    0,
                    11
                ],
                [
                    1,
                    0,
                    10
                ],
                [
                    2,
                    0,
                    9
                ],
                [
                    3,
                    0,
                    10
                ],
                [
                    0,
                    1,
                    12
                ],
                [
                    1,
                    1,
                    12
                ],
                [
                    2,
                    1,
                    4
                ],
                [
                    3,
                    1,
                    6
                ],
                [
                    0,
                    2,
                    8
                ],
                [
                    1,
                    2,
                    9
                ],
                [
                    2,
                    2,
                    12
                ],
                [
                    3,
                    2,
                    5
                ],
                [
                    0,
                    3,
                    1
                ],
                [
                    1,
                    3,
                    11
                ],
                [
                    2,
                    3,
                    7
                ],
                [
                    3,
                    3,
                    12
                ],
                [
                    0,
                    4,
                    7
                ],
                [
                    1,
                    4,
                    4
                ],
                [
                    2,
                    4,
                    10
                ],
                [
                    3,
                    4,
                    8
                ],
                [
                    0,
                    5,
                    5
                ],
                [
                    1,
                    5,
                    1
                ],
                [
                    2,
                    5,
                    11
                ],
                [
                    3,
                    5,
                    11
                ],
                [
                    0,
                    6,
                    9
                ],
                [
                    1,
                    6,
                    3
                ],
                [
                    2,
                    6,
                    5
                ],
                [
                    3,
                    6,
                    7
                ],
                [
                    0,
                    7,
                    6
                ],
                [
                    1,
                    7,
                    5
                ],
                [
                    2,
                    7,
                    8
                ],
                [
                    3,
                    7,
                    3
                ],
                [
                    0,
                    8,
                    3
                ],
                [
                    1,
                    8,
                    6
                ],
                [
                    2,
                    8,
                    3
                ],
                [
                    3,
                    8,
                    9
                ],
                [
                    0,
                    9,
                    10
                ],
                [
                    1,
                    9,
                    2
                ],
                [
                    2,
                    9,
                    6
                ],
                [
                    3,
                    9,
                    2
                ],
                [
                    0,
                    10,
                    1
                ],
                [
                    1,
                    10,
                    7
                ],
                [
                    2,
                    10,
                    2
                ],
                [
                    3,
                    10,
                    4
                ],
                [
                    0,
                    11,
                    4
                ],
                [
                    1,
                    11,
                    8
                ],
                [
                    2,
                    11,
                    1
                ],
                [
                    3,
                    11,
                    1
                ]
            ],
            "label": {
                "show": true,
                "fontSize": 12
            }
        }
    ]
}
```

##### WR
```echarts
{
    "grid": {
        "top": "10%",
        "bottom": "13%",
        "left": "5%",
        "right": "0%",
        "containLabel": true
    },
    "xAxis": {
        "type": "category",
        "data": [
            1,
            2,
            3,
            4
        ],
        "name": "Week",
        "nameLocation": "center",
        "nameGap": 35,
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "yAxis": {
        "type": "category",
        "data": [
            "BTE",
            "TTC",
            "TOM",
            "KTT",
            "90s",
            "TIB",
            "JST",
            "EET",
            "MMT",
            "RRT",
            "HMB",
            "ARV"
        ],
        "name": "",
        "nameLocation": "end",
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "visualMap": {
        "min": 1,
        "max": 12,
        "calculable": true,
        "orient": "vertical",
        "right": "right",
        "show": false,
        "bottom": "30%",
        "text": [],
        "inRange": {
            "color": [
                "#4575b4",
                "#91bfdb",
                "#fee090",
                "#fc8d59",
                "#d73027"
            ]
        }
    },
    "series": [
        {
            "type": "heatmap",
            "data": [
                [
                    0,
                    0,
                    9
                ],
                [
                    1,
                    0,
                    7
                ],
                [
                    2,
                    0,
                    8
                ],
                [
                    3,
                    0,
                    12
                ],
                [
                    0,
                    1,
                    6
                ],
                [
                    1,
                    1,
                    10
                ],
                [
                    2,
                    1,
                    9
                ],
                [
                    3,
                    1,
                    11
                ],
                [
                    0,
                    2,
                    10
                ],
                [
                    1,
                    2,
                    12
                ],
                [
                    2,
                    2,
                    10
                ],
                [
                    3,
                    2,
                    1
                ],
                [
                    0,
                    3,
                    8
                ],
                [
                    1,
                    3,
                    6
                ],
                [
                    2,
                    3,
                    12
                ],
                [
                    3,
                    3,
                    6
                ],
                [
                    0,
                    4,
                    11
                ],
                [
                    1,
                    4,
                    1
                ],
                [
                    2,
                    4,
                    7
                ],
                [
                    3,
                    4,
                    9
                ],
                [
                    0,
                    5,
                    3
                ],
                [
                    1,
                    5,
                    11
                ],
                [
                    2,
                    5,
                    10
                ],
                [
                    3,
                    5,
                    2
                ],
                [
                    0,
                    6,
                    7
                ],
                [
                    1,
                    6,
                    5
                ],
                [
                    2,
                    6,
                    5
                ],
                [
                    3,
                    6,
                    8
                ],
                [
                    0,
                    7,
                    4
                ],
                [
                    1,
                    7,
                    9
                ],
                [
                    2,
                    7,
                    6
                ],
                [
                    3,
                    7,
                    4
                ],
                [
                    0,
                    8,
                    5
                ],
                [
                    1,
                    8,
                    8
                ],
                [
                    2,
                    8,
                    2
                ],
                [
                    3,
                    8,
                    7
                ],
                [
                    0,
                    9,
                    12
                ],
                [
                    1,
                    9,
                    2
                ],
                [
                    2,
                    9,
                    1
                ],
                [
                    3,
                    9,
                    5
                ],
                [
                    0,
                    10,
                    1
                ],
                [
                    1,
                    10,
                    3
                ],
                [
                    2,
                    10,
                    3
                ],
                [
                    3,
                    10,
                    10
                ],
                [
                    0,
                    11,
                    2
                ],
                [
                    1,
                    11,
                    4
                ],
                [
                    2,
                    11,
                    4
                ],
                [
                    3,
                    11,
                    3
                ]
            ],
            "label": {
                "show": true,
                "fontSize": 12
            }
        }
    ]
}
```

##### TE
```echarts
{
    "grid": {
        "top": "10%",
        "bottom": "13%",
        "left": "5%",
        "right": "0%",
        "containLabel": true
    },
    "xAxis": {
        "type": "category",
        "data": [
            1,
            2,
            3,
            4
        ],
        "name": "Week",
        "nameLocation": "center",
        "nameGap": 35,
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "yAxis": {
        "type": "category",
        "data": [
            "ARV",
            "TIB",
            "EET",
            "KTT",
            "BTE",
            "TTC",
            "JST",
            "MMT",
            "HMB",
            "90s",
            "TOM",
            "RRT"
        ],
        "name": "",
        "nameLocation": "end",
        "nameTextStyle": {
            "fontSize": 16
        },
        "axisLabel": {
            "fontSize": 14
        }
    },
    "visualMap": {
        "min": 1,
        "max": 12,
        "calculable": true,
        "orient": "vertical",
        "right": "right",
        "show": false,
        "bottom": "30%",
        "text": [],
        "inRange": {
            "color": [
                "#4575b4",
                "#91bfdb",
                "#fee090",
                "#fc8d59",
                "#d73027"
            ]
        }
    },
    "series": [
        {
            "type": "heatmap",
            "data": [
                [
                    0,
                    0,
                    11
                ],
                [
                    1,
                    0,
                    8
                ],
                [
                    2,
                    0,
                    12
                ],
                [
                    3,
                    0,
                    11
                ],
                [
                    0,
                    1,
                    12
                ],
                [
                    1,
                    1,
                    11
                ],
                [
                    2,
                    1,
                    7
                ],
                [
                    3,
                    1,
                    8
                ],
                [
                    0,
                    2,
                    4
                ],
                [
                    1,
                    2,
                    12
                ],
                [
                    2,
                    2,
                    9
                ],
                [
                    3,
                    2,
                    9
                ],
                [
                    0,
                    3,
                    9
                ],
                [
                    1,
                    3,
                    6
                ],
                [
                    2,
                    3,
                    6
                ],
                [
                    3,
                    3,
                    12
                ],
                [
                    0,
                    4,
                    6
                ],
                [
                    1,
                    4,
                    7
                ],
                [
                    2,
                    4,
                    4
                ],
                [
                    3,
                    4,
                    10
                ],
                [
                    0,
                    5,
                    8
                ],
                [
                    1,
                    5,
                    9
                ],
                [
                    2,
                    5,
                    3
                ],
                [
                    3,
                    5,
                    5
                ],
                [
                    0,
                    6,
                    3
                ],
                [
                    1,
                    6,
                    4
                ],
                [
                    2,
                    6,
                    11
                ],
                [
                    3,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    10
                ],
                [
                    1,
                    7,
                    10
                ],
                [
                    2,
                    7,
                    1
                ],
                [
                    3,
                    7,
                    2
                ],
                [
                    0,
                    8,
                    7
                ],
                [
                    1,
                    8,
                    1
                ],
                [
                    2,
                    8,
                    8
                ],
                [
                    3,
                    8,
                    4
                ],
                [
                    0,
                    9,
                    1
                ],
                [
                    1,
                    9,
                    5
                ],
                [
                    2,
                    9,
                    5
                ],
                [
                    3,
                    9,
                    7
                ],
                [
                    0,
                    10,
                    2
                ],
                [
                    1,
                    10,
                    3
                ],
                [
                    2,
                    10,
                    9
                ],
                [
                    3,
                    10,
                    1
                ],
                [
                    0,
                    11,
                    5
                ],
                [
                    1,
                    11,
                    2
                ],
                [
                    2,
                    11,
                    2
                ],
                [
                    3,
                    11,
                    3
                ]
            ],
            "label": {
                "show": true,
                "fontSize": 12
            }
        }
    ]
}
```


## Advanced Analytics

<br>

### Lineup Efficiency Over Time

```echarts
{
    "title": {
        "text": "Lineup Efficiency Trends",
        "left": "center",
        "show": false
    },
    "tooltip": {
        "trigger": "axis"
    },
    "legend": {
        "data": [
            "90s",
            "HMB",
            "MMT",
            "ARV",
            "TTC",
            "JST",
            "TOM",
            "TIB",
            "KTT",
            "RRT",
            "EET",
            "BTE"
        ],
        "orient": "vertical",
        "right": 0,
        "top": "middle"
    },
    "xAxis": {
        "type": "category",
        "data": [
            "Week 1",
            "Week 2",
            "Week 3",
            "Week 4"
        ]
    },
    "yAxis": {
        "type": "value",
        "name": "Efficiency %"
    },
    "series": [
        {
            "name": "90s",
            "type": "line",
            "data": [
                88.5,
                88.3,
                93.2,
                94.2
            ]
        },
        {
            "name": "HMB",
            "type": "line",
            "data": [
                92.6,
                85.2,
                86.9,
                83.0
            ]
        },
        {
            "name": "MMT",
            "type": "line",
            "data": [
                75.5,
                86.5,
                92.7,
                78.0
            ]
        },
        {
            "name": "ARV",
            "type": "line",
            "data": [
                84.2,
                85.0,
                96.4,
                100.0
            ]
        },
        {
            "name": "TTC",
            "type": "line",
            "data": [
                90.7,
                85.5,
                91.1,
                88.4
            ]
        },
        {
            "name": "JST",
            "type": "line",
            "data": [
                91.7,
                95.2,
                88.0,
                83.4
            ]
        },
        {
            "name": "TOM",
            "type": "line",
            "data": [
                89.1,
                92.5,
                83.6,
                83.3
            ]
        },
        {
            "name": "TIB",
            "type": "line",
            "data": [
                79.6,
                77.4,
                68.0,
                77.5
            ]
        },
        {
            "name": "KTT",
            "type": "line",
            "data": [
                83.0,
                82.6,
                97.1,
                84.6
            ]
        },
        {
            "name": "RRT",
            "type": "line",
            "data": [
                81.4,
                85.3,
                96.9,
                93.0
            ]
        },
        {
            "name": "EET",
            "type": "line",
            "data": [
                88.3,
                66.4,
                97.1,
                78.0
            ]
        },
        {
            "name": "BTE",
            "type": "line",
            "data": [
                77.9,
                74.8,
                79.9,
                76.6
            ]
        }
    ],
    "grid": {
        "right": "10%",
        "left": "5%"
    }
}
```

<br>

### Positional Advantages

```echarts
{
    "tooltip": {
        "trigger": "item"
    },
    "legend": {
        "orient": "vertical",
        "right": 0,
        "top": "middle"
    },
    "radar": {
        "indicator": [
            {
                "name": "QB",
                "max": 20,
                "min": -20
            },
            {
                "name": "RB",
                "max": 20,
                "min": -20
            },
            {
                "name": "WR",
                "max": 20,
                "min": -20
            },
            {
                "name": "TE",
                "max": 20,
                "min": -20
            }
        ]
    },
    "series": [
        {
            "name": "90s MonCon",
            "type": "radar",
            "data": [
                {
                    "value": [
                        4.6,
                        3.6,
                        0.3,
                        2.3
                    ],
                    "name": "90s MonCon"
                }
            ]
        },
        {
            "name": "Game of Zones - House Hamlin",
            "type": "radar",
            "data": [
                {
                    "value": [
                        6.3,
                        -1.0,
                        5.8,
                        2.8
                    ],
                    "name": "Game of Zones - House Hamlin"
                }
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        5.6,
                        0.1,
                        1.4,
                        -1.0
                    ],
                    "name": "Michael's Managable Team"
                }
            ]
        },
        {
            "name": "Abbey's TNT Team ",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -4.2,
                        3.6,
                        3.0,
                        -5.4
                    ],
                    "name": "Abbey's TNT Team "
                }
            ]
        },
        {
            "name": "Third Time's the Charm?",
            "type": "radar",
            "data": [
                {
                    "value": [
                        1.6,
                        -0.3,
                        -3.2,
                        -0.4
                    ],
                    "name": "Third Time's the Charm?"
                }
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "radar",
            "data": [
                {
                    "value": [
                        3.9,
                        2.5,
                        0.8,
                        1.4
                    ],
                    "name": "Mama Daughter Duo"
                }
            ]
        },
        {
            "name": "Rookie Mistake",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -2.5,
                        1.3,
                        -2.8,
                        3.2
                    ],
                    "name": "Rookie Mistake"
                }
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -0.7,
                        0.8,
                        1.7,
                        -5.1
                    ],
                    "name": "To Infinity and Bijan!"
                }
            ]
        },
        {
            "name": "Mcconky Donkeys",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -0.0,
                        -2.9,
                        -2.9,
                        -1.9
                    ],
                    "name": "Mcconky Donkeys"
                }
            ]
        },
        {
            "name": "Americas Team ",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -2.3,
                        1.2,
                        -0.3,
                        3.6
                    ],
                    "name": "Americas Team "
                }
            ]
        },
        {
            "name": "Emma's Excellent Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -6.7,
                        -2.9,
                        -0.5,
                        -1.8
                    ],
                    "name": "Emma's Excellent Team"
                }
            ]
        },
        {
            "name": "Big Titi Energy",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -7.7,
                        -3.9,
                        -3.8,
                        0.2
                    ],
                    "name": "Big Titi Energy"
                }
            ]
        }
    ]
}
```

