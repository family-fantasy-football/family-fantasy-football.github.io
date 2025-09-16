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


The current top scorer is: Kyle Hamlin (296.13)

The current bottom scorer is: Christine Hamlin (150.69)

Highest Scoring Week: Kyle Hamlin - 176.38 points (Week 1)

Lowest Scoring Week: Emma Grau - 67.94 points (Week 2)

Luckiest Team: Christian Ratcliff (0.8) Wins Above Expected

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
            2
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
                "color": "#98df8a"
            },
            "itemStyle": {
                "color": "#98df8a"
            },
            "data": [
                7,
                4
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
                "color": "#c49c94"
            },
            "itemStyle": {
                "color": "#c49c94"
            },
            "data": [
                4,
                8
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
            "name": "Fantasy Guru Kayden",
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
                9
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Fantasy Guru..."
            }
        },
        {
            "name": "Game of Zones - House Hamlin",
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
                1,
                1
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
                "color": "#d62728"
            },
            "itemStyle": {
                "color": "#d62728"
            },
            "data": [
                3,
                5
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
            "name": "Michael's Managable Team",
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
                5,
                2
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
                "color": "#ffbb78"
            },
            "itemStyle": {
                "color": "#ffbb78"
            },
            "data": [
                6,
                3
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
                "color": "#9467bd"
            },
            "itemStyle": {
                "color": "#9467bd"
            },
            "data": [
                2,
                6
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
        "min": 1.0,
        "max": 452.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": 1.0,
        "max": 452.0
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
                        218.01,
                        191.53
                    ]
                },
                {
                    "name": "90s MonCon",
                    "value": [
                        268.62,
                        260.57
                    ]
                },
                {
                    "name": "Rookie Mistake",
                    "value": [
                        228.87,
                        195.48
                    ]
                },
                {
                    "name": "Americas Team ",
                    "value": [
                        228.72,
                        263.29
                    ]
                },
                {
                    "name": "Michael's Managable Team",
                    "value": [
                        252.98,
                        237.69
                    ]
                },
                {
                    "name": "To Infinity and Bijan!",
                    "value": [
                        245.52,
                        213.02
                    ]
                },
                {
                    "name": "Fantasy Guru Kayden",
                    "value": [
                        200.55,
                        202.03
                    ]
                },
                {
                    "name": "Mama Daughter Duo",
                    "value": [
                        252.6,
                        244.7
                    ]
                },
                {
                    "name": "Abbey's TNT Team ",
                    "value": [
                        228.81,
                        227.95
                    ]
                },
                {
                    "name": "Game of Zones - House Hamlin",
                    "value": [
                        296.13,
                        194.68
                    ]
                },
                {
                    "name": "Emma's Excellent Team",
                    "value": [
                        176.14,
                        215.12
                    ]
                },
                {
                    "name": "Big Titi Energy",
                    "value": [
                        150.69,
                        301.58
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
                    1.0,
                    1.0
                ],
                [
                    452.0,
                    452.0
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
                        "xAxis": 228.97,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 228.97,
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
            "HMB",
            "MMT",
            "TTC",
            "90s",
            "JST",
            "TIB",
            "TOM",
            "ARV",
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
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
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
                    176.38,
                    "HMB"
                ],
                [
                    0,
                    119.75,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    111.95,
                    "MMT"
                ],
                [
                    1,
                    141.03,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    1,
                    0.0,
                    "MMT"
                ],
                [
                    2,
                    106.14,
                    "TTC"
                ],
                [
                    2,
                    111.87,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    2,
                    0.0,
                    "TTC"
                ],
                [
                    3,
                    111.47,
                    "90s"
                ],
                [
                    3,
                    157.15,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    3,
                    0.0,
                    "90s"
                ],
                [
                    4,
                    126.38,
                    "JST"
                ],
                [
                    4,
                    126.22,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    4,
                    0.0,
                    "JST"
                ],
                [
                    5,
                    134.09,
                    "TIB"
                ],
                [
                    5,
                    111.43,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    0.0,
                    "TIB"
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
                    115.72,
                    "ARV"
                ],
                [
                    7,
                    113.09,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
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
            "HMB",
            "MMT",
            "TTC",
            "90s",
            "JST",
            "TIB",
            "TOM",
            "ARV",
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
                    3
                ],
                [
                    1,
                    0,
                    8
                ],
                [
                    2,
                    0,
                    1
                ],
                [
                    3,
                    0,
                    1
                ],
                [
                    0,
                    1,
                    1
                ],
                [
                    1,
                    1,
                    7
                ],
                [
                    2,
                    1,
                    11
                ],
                [
                    3,
                    1,
                    5
                ],
                [
                    0,
                    2,
                    5
                ],
                [
                    1,
                    2,
                    9
                ],
                [
                    2,
                    2,
                    8
                ],
                [
                    3,
                    2,
                    8
                ],
                [
                    0,
                    3,
                    2
                ],
                [
                    1,
                    3,
                    3
                ],
                [
                    2,
                    3,
                    4
                ],
                [
                    3,
                    3,
                    7
                ],
                [
                    0,
                    4,
                    6
                ],
                [
                    1,
                    4,
                    2
                ],
                [
                    2,
                    4,
                    5
                ],
                [
                    3,
                    4,
                    4
                ],
                [
                    0,
                    5,
                    8
                ],
                [
                    1,
                    5,
                    4
                ],
                [
                    2,
                    5,
                    12
                ],
                [
                    3,
                    5,
                    2
                ],
                [
                    0,
                    6,
                    4
                ],
                [
                    1,
                    6,
                    6
                ],
                [
                    2,
                    6,
                    2
                ],
                [
                    3,
                    6,
                    12
                ],
                [
                    0,
                    7,
                    11
                ],
                [
                    1,
                    7,
                    1
                ],
                [
                    2,
                    7,
                    10
                ],
                [
                    3,
                    7,
                    3
                ],
                [
                    0,
                    8,
                    7
                ],
                [
                    1,
                    8,
                    11
                ],
                [
                    2,
                    8,
                    7
                ],
                [
                    3,
                    8,
                    10
                ],
                [
                    0,
                    9,
                    9
                ],
                [
                    1,
                    9,
                    5
                ],
                [
                    2,
                    9,
                    3
                ],
                [
                    3,
                    9,
                    6
                ],
                [
                    0,
                    10,
                    10
                ],
                [
                    1,
                    10,
                    10
                ],
                [
                    2,
                    10,
                    9
                ],
                [
                    3,
                    10,
                    9
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
                    6
                ],
                [
                    3,
                    11,
                    11
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
            2
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
            "ARV",
            "RRT",
            "90s",
            "BTE",
            "TIB",
            "TTC",
            "HMB",
            "JST",
            "MMT",
            "KTT",
            "TOM"
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
                    0,
                    1,
                    6
                ],
                [
                    1,
                    1,
                    12
                ],
                [
                    0,
                    2,
                    10
                ],
                [
                    1,
                    2,
                    7
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
                    0,
                    4,
                    2
                ],
                [
                    1,
                    4,
                    10
                ],
                [
                    0,
                    5,
                    1
                ],
                [
                    1,
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
                    0,
                    8,
                    3
                ],
                [
                    1,
                    8,
                    8
                ],
                [
                    0,
                    9,
                    8
                ],
                [
                    1,
                    9,
                    2
                ],
                [
                    0,
                    10,
                    4
                ],
                [
                    1,
                    10,
                    5
                ],
                [
                    0,
                    11,
                    7
                ],
                [
                    1,
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
            2
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
            "EET",
            "KTT",
            "HMB",
            "90s",
            "RRT",
            "TOM",
            "JST",
            "MMT",
            "ARV",
            "TTC",
            "TIB"
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
                    12
                ],
                [
                    1,
                    0,
                    12
                ],
                [
                    0,
                    1,
                    11
                ],
                [
                    1,
                    1,
                    10
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
                    0,
                    4,
                    4
                ],
                [
                    1,
                    4,
                    8
                ],
                [
                    0,
                    5,
                    10
                ],
                [
                    1,
                    5,
                    2
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
                    0,
                    8,
                    7
                ],
                [
                    1,
                    8,
                    4
                ],
                [
                    0,
                    9,
                    3
                ],
                [
                    1,
                    9,
                    6
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
                    0,
                    11,
                    5
                ],
                [
                    1,
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
            2
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
            "TOM",
            "BTE",
            "TTC",
            "KTT",
            "RRT",
            "TIB",
            "EET",
            "MMT",
            "90s",
            "JST",
            "ARV",
            "HMB"
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
                    10
                ],
                [
                    1,
                    0,
                    12
                ],
                [
                    0,
                    1,
                    9
                ],
                [
                    1,
                    1,
                    7
                ],
                [
                    0,
                    2,
                    6
                ],
                [
                    1,
                    2,
                    10
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
                    0,
                    4,
                    12
                ],
                [
                    1,
                    4,
                    2
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
                    0,
                    6,
                    4
                ],
                [
                    1,
                    6,
                    9
                ],
                [
                    0,
                    7,
                    5
                ],
                [
                    1,
                    7,
                    8
                ],
                [
                    0,
                    8,
                    11
                ],
                [
                    1,
                    8,
                    1
                ],
                [
                    0,
                    9,
                    7
                ],
                [
                    1,
                    9,
                    5
                ],
                [
                    0,
                    10,
                    2
                ],
                [
                    1,
                    10,
                    4
                ],
                [
                    0,
                    11,
                    1
                ],
                [
                    1,
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
            2
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
            "TIB",
            "MMT",
            "ARV",
            "TTC",
            "EET",
            "KTT",
            "BTE",
            "HMB",
            "JST",
            "RRT",
            "90s",
            "TOM"
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
                    12
                ],
                [
                    1,
                    0,
                    11
                ],
                [
                    0,
                    1,
                    10
                ],
                [
                    1,
                    1,
                    10
                ],
                [
                    0,
                    2,
                    11
                ],
                [
                    1,
                    2,
                    8
                ],
                [
                    0,
                    3,
                    8
                ],
                [
                    1,
                    3,
                    9
                ],
                [
                    0,
                    4,
                    4
                ],
                [
                    1,
                    4,
                    12
                ],
                [
                    0,
                    5,
                    9
                ],
                [
                    1,
                    5,
                    6
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    1,
                    6,
                    7
                ],
                [
                    0,
                    7,
                    7
                ],
                [
                    1,
                    7,
                    1
                ],
                [
                    0,
                    8,
                    3
                ],
                [
                    1,
                    8,
                    4
                ],
                [
                    0,
                    9,
                    5
                ],
                [
                    1,
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
                    5
                ],
                [
                    0,
                    11,
                    2
                ],
                [
                    1,
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
            "HMB",
            "MMT",
            "TTC",
            "90s",
            "JST",
            "TIB",
            "TOM",
            "ARV",
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
            "Week 2"
        ]
    },
    "yAxis": {
        "type": "value",
        "name": "Efficiency %"
    },
    "series": [
        {
            "name": "HMB",
            "type": "line",
            "data": [
                92.6,
                85.2
            ]
        },
        {
            "name": "MMT",
            "type": "line",
            "data": [
                75.5,
                86.5
            ]
        },
        {
            "name": "TTC",
            "type": "line",
            "data": [
                90.7,
                85.5
            ]
        },
        {
            "name": "90s",
            "type": "line",
            "data": [
                88.5,
                88.3
            ]
        },
        {
            "name": "JST",
            "type": "line",
            "data": [
                91.7,
                95.2
            ]
        },
        {
            "name": "TIB",
            "type": "line",
            "data": [
                79.6,
                77.4
            ]
        },
        {
            "name": "TOM",
            "type": "line",
            "data": [
                89.1,
                92.5
            ]
        },
        {
            "name": "ARV",
            "type": "line",
            "data": [
                84.2,
                85.0
            ]
        },
        {
            "name": "KTT",
            "type": "line",
            "data": [
                83.0,
                82.6
            ]
        },
        {
            "name": "RRT",
            "type": "line",
            "data": [
                81.4,
                85.3
            ]
        },
        {
            "name": "EET",
            "type": "line",
            "data": [
                88.3,
                66.4
            ]
        },
        {
            "name": "BTE",
            "type": "line",
            "data": [
                77.9,
                74.8
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
            "name": "Game of Zones - House Hamlin",
            "type": "radar",
            "data": [
                {
                    "value": [
                        7.4,
                        2.2,
                        7.9,
                        3.6
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
                        7.6,
                        -0.5,
                        -0.5,
                        -5.2
                    ],
                    "name": "Michael's Managable Team"
                }
            ]
        },
        {
            "name": "Third Time's the Charm?",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -0.3,
                        0.1,
                        -1.8,
                        -1.1
                    ],
                    "name": "Third Time's the Charm?"
                }
            ]
        },
        {
            "name": "90s MonCon",
            "type": "radar",
            "data": [
                {
                    "value": [
                        3.8,
                        2.0,
                        -0.8,
                        3.6
                    ],
                    "name": "90s MonCon"
                }
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "radar",
            "data": [
                {
                    "value": [
                        2.4,
                        2.4,
                        0.1,
                        2.9
                    ],
                    "name": "Mama Daughter Duo"
                }
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "radar",
            "data": [
                {
                    "value": [
                        1.5,
                        1.4,
                        3.6,
                        -7.1
                    ],
                    "name": "To Infinity and Bijan!"
                }
            ]
        },
        {
            "name": "Rookie Mistake",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -1.1,
                        0.5,
                        -3.1,
                        4.1
                    ],
                    "name": "Rookie Mistake"
                }
            ]
        },
        {
            "name": "Abbey's TNT Team ",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -6.8,
                        4.3,
                        2.9,
                        -4.9
                    ],
                    "name": "Abbey's TNT Team "
                }
            ]
        },
        {
            "name": "Fantasy Guru Kayden",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.8,
                        -2.9,
                        -1.8,
                        -2.0
                    ],
                    "name": "Fantasy Guru Kayden"
                }
            ]
        },
        {
            "name": "Americas Team ",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -5.0,
                        1.0,
                        -1.7,
                        2.9
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
                        -4.4,
                        -2.5,
                        -0.4,
                        -0.6
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
                        -6.5,
                        -4.7,
                        -3.6,
                        0.4
                    ],
                    "name": "Big Titi Energy"
                }
            ]
        }
    ]
}
```

