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


The current top scorer is: Kyle Hamlin (176.38)

The current bottom scorer is: Ryan Ratcliff (80.10)

Highest Scoring Week: Kyle Hamlin - 176.38 points (Week 1)

Lowest Scoring Week: Ryan Ratcliff - 80.10 points (Week 1)

Luckiest Team: Christian Ratcliff (1.0) Wins Above Expected

Unluckiest Team: Connor Dickson and Monika Monko (-0.0) Wins Below Expected




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
            1
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
                "color": "#8c564b"
            },
            "itemStyle": {
                "color": "#8c564b"
            },
            "data": [
                7
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
                "color": "#17becf"
            },
            "itemStyle": {
                "color": "#17becf"
            },
            "data": [
                12
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
                "color": "#bcbd22"
            },
            "itemStyle": {
                "color": "#bcbd22"
            },
            "data": [
                11
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
                "color": "#c49c94"
            },
            "itemStyle": {
                "color": "#c49c94"
            },
            "data": [
                8
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
                "color": "#c7c7c7"
            },
            "itemStyle": {
                "color": "#c7c7c7"
            },
            "data": [
                10
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
                "color": "#ffbb78"
            },
            "itemStyle": {
                "color": "#ffbb78"
            },
            "data": [
                3
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
                "color": "#d62728"
            },
            "itemStyle": {
                "color": "#d62728"
            },
            "data": [
                5
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
                "color": "#f7b6d2"
            },
            "itemStyle": {
                "color": "#f7b6d2"
            },
            "data": [
                9
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
                "color": "#9467bd"
            },
            "itemStyle": {
                "color": "#9467bd"
            },
            "data": [
                6
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
                "color": "#aec7e8"
            },
            "itemStyle": {
                "color": "#aec7e8"
            },
            "data": [
                2
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
        "min": -70.0,
        "max": 326.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": -70.0,
        "max": 326.0
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
                        106.14,
                        80.1
                    ]
                },
                {
                    "name": "90s MonCon",
                    "value": [
                        111.47,
                        111.95
                    ]
                },
                {
                    "name": "Rookie Mistake",
                    "value": [
                        103.67,
                        126.38
                    ]
                },
                {
                    "name": "Americas Team ",
                    "value": [
                        80.1,
                        106.14
                    ]
                },
                {
                    "name": "Michael's Managable Team",
                    "value": [
                        111.95,
                        111.47
                    ]
                },
                {
                    "name": "To Infinity and Bijan!",
                    "value": [
                        134.09,
                        101.15
                    ]
                },
                {
                    "name": "Fantasy Guru Kayden",
                    "value": [
                        101.15,
                        134.09
                    ]
                },
                {
                    "name": "Mama Daughter Duo",
                    "value": [
                        126.38,
                        103.67
                    ]
                },
                {
                    "name": "Abbey's TNT Team ",
                    "value": [
                        115.72,
                        108.2
                    ]
                },
                {
                    "name": "Game of Zones - House Hamlin",
                    "value": [
                        176.38,
                        81.59
                    ]
                },
                {
                    "name": "Emma's Excellent Team",
                    "value": [
                        108.2,
                        115.72
                    ]
                },
                {
                    "name": "Big Titi Energy",
                    "value": [
                        81.59,
                        176.38
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
                    -70.0,
                    -70.0
                ],
                [
                    326.0,
                    326.0
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
                        "xAxis": 113.07,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 113.07,
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
            "TIB",
            "JST",
            "ARV",
            "MMT",
            "TTC",
            "90s",
            "EET",
            "TOM",
            "KTT",
            "BTE",
            "RRT"
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
                    0,
                    0.0,
                    "HMB"
                ],
                [
                    1,
                    134.09,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    1,
                    0.0,
                    "TIB"
                ],
                [
                    2,
                    126.38,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    2,
                    0.0,
                    "JST"
                ],
                [
                    3,
                    115.72,
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
                    111.95,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    4,
                    0.0,
                    "MMT"
                ],
                [
                    5,
                    106.14,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    5,
                    0.0,
                    "TTC"
                ],
                [
                    6,
                    111.47,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    6,
                    0.0,
                    "90s"
                ],
                [
                    7,
                    108.2,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    7,
                    0.0,
                    "EET"
                ],
                [
                    8,
                    103.67,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    8,
                    0.0,
                    "TOM"
                ],
                [
                    9,
                    101.15,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
                ],
                [
                    10,
                    81.59,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    10,
                    0.0,
                    "BTE"
                ],
                [
                    11,
                    80.1,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
                ],
                [
                    11,
                    0.0,
                    "RRT"
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
            "TIB",
            "JST",
            "ARV",
            "MMT",
            "TTC",
            "90s",
            "EET",
            "TOM",
            "KTT",
            "BTE",
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
                    1
                ],
                [
                    1,
                    0,
                    1
                ],
                [
                    2,
                    0,
                    5
                ],
                [
                    3,
                    0,
                    1
                ],
                [
                    0,
                    1,
                    2
                ],
                [
                    1,
                    1,
                    8
                ],
                [
                    2,
                    1,
                    12
                ],
                [
                    3,
                    1,
                    2
                ],
                [
                    0,
                    2,
                    4
                ],
                [
                    1,
                    2,
                    3
                ],
                [
                    2,
                    2,
                    3
                ],
                [
                    3,
                    2,
                    6
                ],
                [
                    0,
                    3,
                    11
                ],
                [
                    1,
                    3,
                    2
                ],
                [
                    2,
                    3,
                    11
                ],
                [
                    3,
                    3,
                    4
                ],
                [
                    0,
                    4,
                    3
                ],
                [
                    1,
                    4,
                    9
                ],
                [
                    2,
                    4,
                    10
                ],
                [
                    3,
                    4,
                    9
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
                    8
                ],
                [
                    3,
                    5,
                    10
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    1,
                    6,
                    6
                ],
                [
                    2,
                    6,
                    1
                ],
                [
                    3,
                    6,
                    8
                ],
                [
                    0,
                    7,
                    9
                ],
                [
                    1,
                    7,
                    10
                ],
                [
                    2,
                    7,
                    4
                ],
                [
                    3,
                    7,
                    3
                ],
                [
                    0,
                    8,
                    10
                ],
                [
                    1,
                    8,
                    5
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
                    5
                ],
                [
                    1,
                    9,
                    11
                ],
                [
                    2,
                    9,
                    9
                ],
                [
                    3,
                    9,
                    5
                ],
                [
                    0,
                    10,
                    7
                ],
                [
                    1,
                    10,
                    12
                ],
                [
                    2,
                    10,
                    7
                ],
                [
                    3,
                    10,
                    12
                ],
                [
                    0,
                    11,
                    12
                ],
                [
                    1,
                    11,
                    7
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
            1
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
            "90s",
            "EET",
            "RRT",
            "TTC",
            "MMT",
            "TOM",
            "ARV",
            "HMB",
            "KTT",
            "JST",
            "BTE",
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
                    0,
                    1,
                    11
                ],
                [
                    0,
                    2,
                    10
                ],
                [
                    0,
                    3,
                    9
                ],
                [
                    0,
                    4,
                    8
                ],
                [
                    0,
                    5,
                    7
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    5
                ],
                [
                    0,
                    8,
                    4
                ],
                [
                    0,
                    9,
                    3
                ],
                [
                    0,
                    10,
                    2
                ],
                [
                    0,
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
            1
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
            "RRT",
            "TOM",
            "KTT",
            "MMT",
            "JST",
            "TIB",
            "90s",
            "ARV",
            "HMB",
            "TTC"
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
                    0,
                    1,
                    11
                ],
                [
                    0,
                    2,
                    10
                ],
                [
                    0,
                    3,
                    9
                ],
                [
                    0,
                    4,
                    8
                ],
                [
                    0,
                    5,
                    7
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    5
                ],
                [
                    0,
                    8,
                    4
                ],
                [
                    0,
                    9,
                    3
                ],
                [
                    0,
                    10,
                    1
                ],
                [
                    0,
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
            1
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
            "RRT",
            "90s",
            "TOM",
            "BTE",
            "KTT",
            "JST",
            "TTC",
            "MMT",
            "EET",
            "TIB",
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
                    12
                ],
                [
                    0,
                    1,
                    11
                ],
                [
                    0,
                    2,
                    10
                ],
                [
                    0,
                    3,
                    9
                ],
                [
                    0,
                    4,
                    8
                ],
                [
                    0,
                    5,
                    7
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    5
                ],
                [
                    0,
                    8,
                    4
                ],
                [
                    0,
                    9,
                    3
                ],
                [
                    0,
                    10,
                    2
                ],
                [
                    0,
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
            1
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
            "ARV",
            "MMT",
            "KTT",
            "TTC",
            "HMB",
            "BTE",
            "RRT",
            "EET",
            "JST",
            "TOM",
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
                    12
                ],
                [
                    0,
                    1,
                    11
                ],
                [
                    0,
                    2,
                    10
                ],
                [
                    0,
                    3,
                    9
                ],
                [
                    0,
                    4,
                    8
                ],
                [
                    0,
                    5,
                    7
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    5
                ],
                [
                    0,
                    8,
                    4
                ],
                [
                    0,
                    9,
                    3
                ],
                [
                    0,
                    10,
                    2
                ],
                [
                    0,
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
            "TIB",
            "JST",
            "ARV",
            "MMT",
            "TTC",
            "90s",
            "EET",
            "TOM",
            "KTT",
            "BTE",
            "RRT"
        ],
        "orient": "vertical",
        "right": 0,
        "top": "middle"
    },
    "xAxis": {
        "type": "category",
        "data": [
            "Week 1"
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
                92.6
            ]
        },
        {
            "name": "TIB",
            "type": "line",
            "data": [
                79.6
            ]
        },
        {
            "name": "JST",
            "type": "line",
            "data": [
                91.7
            ]
        },
        {
            "name": "ARV",
            "type": "line",
            "data": [
                84.2
            ]
        },
        {
            "name": "MMT",
            "type": "line",
            "data": [
                75.5
            ]
        },
        {
            "name": "TTC",
            "type": "line",
            "data": [
                90.7
            ]
        },
        {
            "name": "90s",
            "type": "line",
            "data": [
                88.5
            ]
        },
        {
            "name": "EET",
            "type": "line",
            "data": [
                88.3
            ]
        },
        {
            "name": "TOM",
            "type": "line",
            "data": [
                89.1
            ]
        },
        {
            "name": "KTT",
            "type": "line",
            "data": [
                83.0
            ]
        },
        {
            "name": "BTE",
            "type": "line",
            "data": [
                77.9
            ]
        },
        {
            "name": "RRT",
            "type": "line",
            "data": [
                81.4
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
                        13.3,
                        6.6,
                        6.1,
                        2.0
                    ],
                    "name": "Game of Zones - House Hamlin"
                }
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "radar",
            "data": [
                {
                    "value": [
                        8.4,
                        -1.0,
                        3.8,
                        -7.6
                    ],
                    "name": "To Infinity and Bijan!"
                }
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "radar",
            "data": [
                {
                    "value": [
                        5.5,
                        1.6,
                        -0.7,
                        3.3
                    ],
                    "name": "Mama Daughter Duo"
                }
            ]
        },
        {
            "name": "Abbey's TNT Team ",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -6.9,
                        5.6,
                        3.2,
                        -6.2
                    ],
                    "name": "Abbey's TNT Team "
                }
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        6.1,
                        -1.8,
                        -1.3,
                        -5.1
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
                        -3.3,
                        1.1,
                        -1.6,
                        0.0
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
                        -0.5,
                        0.3,
                        -1.3,
                        5.2
                    ],
                    "name": "90s MonCon"
                }
            ]
        },
        {
            "name": "Emma's Excellent Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -5.7,
                        -2.4,
                        3.3,
                        2.6
                    ],
                    "name": "Emma's Excellent Team"
                }
            ]
        },
        {
            "name": "Rookie Mistake",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -6.2,
                        0.5,
                        -1.3,
                        4.3
                    ],
                    "name": "Rookie Mistake"
                }
            ]
        },
        {
            "name": "Fantasy Guru Kayden",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.6,
                        -3.1,
                        -0.6,
                        -2.9
                    ],
                    "name": "Fantasy Guru Kayden"
                }
            ]
        },
        {
            "name": "Big Titi Energy",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -2.8,
                        -5.0,
                        -4.2,
                        0.8
                    ],
                    "name": "Big Titi Energy"
                }
            ]
        },
        {
            "name": "Americas Team ",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -8.5,
                        -0.4,
                        -3.9,
                        1.7
                    ],
                    "name": "Americas Team "
                }
            ]
        }
    ]
}
```

