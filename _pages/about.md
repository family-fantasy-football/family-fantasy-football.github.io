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


The current top scorer is: Connor Dickson and Monika Monko (714.78)

The current bottom scorer is: Emma Grau (460.97)

Highest Scoring Week: Ryan Ratcliff - 178.27 points (Week 5)

Lowest Scoring Week: Emma Grau - 67.94 points (Week 2)

Luckiest Team: Kayden Mullins (1.5) Wins Above Expected

Unluckiest Team: Ryan Ratcliff (-1.3) Wins Below Expected




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
            4,
            5
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
                "color": "#ffbb78"
            },
            "itemStyle": {
                "color": "#ffbb78"
            },
            "data": [
                7,
                4,
                3,
                1,
                3
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
                "color": "#d62728"
            },
            "itemStyle": {
                "color": "#d62728"
            },
            "data": [
                4,
                8,
                5,
                4,
                5
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
                "color": "#c49c94"
            },
            "itemStyle": {
                "color": "#c49c94"
            },
            "data": [
                12,
                10,
                10,
                10,
                8
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
                11,
                12,
                12,
                12,
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
                "color": "#17becf"
            },
            "itemStyle": {
                "color": "#17becf"
            },
            "data": [
                8,
                11,
                11,
                11,
                12
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
                "color": "#1f77b4"
            },
            "itemStyle": {
                "color": "#1f77b4"
            },
            "data": [
                1,
                1,
                1,
                2,
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
                "color": "#f7b6d2"
            },
            "itemStyle": {
                "color": "#f7b6d2"
            },
            "data": [
                3,
                5,
                4,
                6,
                9
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
                "color": "#8c564b"
            },
            "itemStyle": {
                "color": "#8c564b"
            },
            "data": [
                10,
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
                "formatter": "Mcconky Donk..."
            }
        },
        {
            "name": "Michael's Managable Team",
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
                5,
                2,
                2,
                3,
                4
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
                "color": "#9467bd"
            },
            "itemStyle": {
                "color": "#9467bd"
            },
            "data": [
                9,
                7,
                9,
                7,
                6
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
                "color": "#aec7e8"
            },
            "itemStyle": {
                "color": "#aec7e8"
            },
            "data": [
                6,
                3,
                6,
                5,
                2
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
                "color": "#c7c7c7"
            },
            "itemStyle": {
                "color": "#c7c7c7"
            },
            "data": [
                2,
                6,
                8,
                8,
                10
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
        "formatter": "{a}"
    },
    "legend": {
        "orient": "vertical",
        "right": "2%",
        "top": "middle",
        "data": [
            "Third Time's the Charm?",
            "90s MonCon",
            "Rookie Mistake",
            "Americas Team ",
            "Michael's Managable Team",
            "To Infinity and Bijan!",
            "Mcconky Donkeys",
            "Mama Daughter Duo",
            "Abbey's TNT Team ",
            "Game of Zones - House Hamlin",
            "Emma's Excellent Team",
            "Big Titi Energy"
        ]
    },
    "xAxis": {
        "type": "value",
        "name": "Points For",
        "nameLocation": "middle",
        "nameGap": 30,
        "min": 311.0,
        "max": 865.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": 311.0,
        "max": 865.0
    },
    "series": [
        {
            "name": "Third Time's the Charm?",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    625.62,
                    545.61
                ]
            ]
        },
        {
            "name": "90s MonCon",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    714.78,
                    591.36
                ]
            ]
        },
        {
            "name": "Rookie Mistake",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    600.01,
                    556.04
                ]
            ]
        },
        {
            "name": "Americas Team ",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    663.13,
                    648.67
                ]
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    658.45,
                    599.39
                ]
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    593.87,
                    655.36
                ]
            ]
        },
        {
            "name": "Mcconky Donkeys",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    505.64,
                    523.49
                ]
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    653.74,
                    656.66
                ]
            ]
        },
        {
            "name": "Abbey's TNT Team ",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    652.26,
                    637.64
                ]
            ]
        },
        {
            "name": "Game of Zones - House Hamlin",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    669.18,
                    544.43
                ]
            ]
        },
        {
            "name": "Emma's Excellent Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    460.97,
                    607.32
                ]
            ]
        },
        {
            "name": "Big Titi Energy",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    462.32,
                    694.0
                ]
            ]
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
                    311.0,
                    311.0
                ],
                [
                    865.0,
                    865.0
                ]
            ],
            "silent": true
        },
        {
            "name": "Average Lines",
            "type": "line",
            "markLine": {
                "silent": true,
                "data": [
                    {
                        "xAxis": 605.0,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 605.0,
                        "lineStyle": {
                            "color": "red",
                            "opacity": 0.5
                        }
                    }
                ]
            },
            "silent": true
        }
    ],
    "grid": {
        "left": "0%",
        "right": "26%",
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
            "TTC",
            "90s",
            "MMT",
            "ARV",
            "TOM",
            "KTT",
            "RRT",
            "JST",
            "TIB",
            "BTE",
            "EET"
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
                    114.94,
                    119.75,
                    122.87,
                    135.24,
                    158.48
                ],
                [
                    85.3,
                    106.14,
                    111.87,
                    156.86,
                    165.45
                ],
                [
                    111.47,
                    115.91,
                    157.15,
                    159.49,
                    170.76
                ],
                [
                    111.95,
                    119.91,
                    136.89,
                    141.03,
                    148.67
                ],
                [
                    113.09,
                    115.72,
                    120.18,
                    145.7,
                    157.57
                ],
                [
                    94.53,
                    103.67,
                    120.4,
                    125.2,
                    156.21
                ],
                [
                    86.76,
                    88.53,
                    99.4,
                    101.15,
                    120.08
                ],
                [
                    80.1,
                    111.53,
                    144.61,
                    148.62,
                    178.27
                ],
                [
                    120.25,
                    123.73,
                    126.22,
                    126.38,
                    130.35
                ],
                [
                    78.58,
                    111.43,
                    132.22,
                    134.09,
                    137.55
                ],
                [
                    79.37,
                    81.26,
                    81.59,
                    82.52,
                    84.41
                ],
                [
                    67.94,
                    73.63,
                    105.14,
                    106.06,
                    108.2
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
                    114.94,
                    "HMB"
                ],
                [
                    0,
                    135.24,
                    "HMB"
                ],
                [
                    0,
                    122.87,
                    "HMB"
                ],
                [
                    1,
                    106.14,
                    "TTC"
                ],
                [
                    1,
                    111.87,
                    "TTC"
                ],
                [
                    1,
                    85.3,
                    "TTC"
                ],
                [
                    1,
                    156.86,
                    "TTC"
                ],
                [
                    1,
                    165.45,
                    "TTC"
                ],
                [
                    2,
                    111.47,
                    "90s"
                ],
                [
                    2,
                    157.15,
                    "90s"
                ],
                [
                    2,
                    170.76,
                    "90s"
                ],
                [
                    2,
                    115.91,
                    "90s"
                ],
                [
                    2,
                    159.49,
                    "90s"
                ],
                [
                    3,
                    111.95,
                    "MMT"
                ],
                [
                    3,
                    141.03,
                    "MMT"
                ],
                [
                    3,
                    148.67,
                    "MMT"
                ],
                [
                    3,
                    136.89,
                    "MMT"
                ],
                [
                    3,
                    119.91,
                    "MMT"
                ],
                [
                    4,
                    115.72,
                    "ARV"
                ],
                [
                    4,
                    113.09,
                    "ARV"
                ],
                [
                    4,
                    120.18,
                    "ARV"
                ],
                [
                    4,
                    157.57,
                    "ARV"
                ],
                [
                    4,
                    145.7,
                    "ARV"
                ],
                [
                    5,
                    103.67,
                    "TOM"
                ],
                [
                    5,
                    125.2,
                    "TOM"
                ],
                [
                    5,
                    94.53,
                    "TOM"
                ],
                [
                    5,
                    156.21,
                    "TOM"
                ],
                [
                    5,
                    120.4,
                    "TOM"
                ],
                [
                    6,
                    101.15,
                    "KTT"
                ],
                [
                    6,
                    99.4,
                    "KTT"
                ],
                [
                    6,
                    88.53,
                    "KTT"
                ],
                [
                    6,
                    86.76,
                    "KTT"
                ],
                [
                    6,
                    129.8,
                    "KTT"
                ],
                [
                    7,
                    80.1,
                    "RRT"
                ],
                [
                    7,
                    148.62,
                    "RRT"
                ],
                [
                    7,
                    144.61,
                    "RRT"
                ],
                [
                    7,
                    111.53,
                    "RRT"
                ],
                [
                    7,
                    178.27,
                    "RRT"
                ],
                [
                    8,
                    126.38,
                    "JST"
                ],
                [
                    8,
                    126.22,
                    "JST"
                ],
                [
                    8,
                    157.16,
                    "JST"
                ],
                [
                    8,
                    123.73,
                    "JST"
                ],
                [
                    8,
                    120.25,
                    "JST"
                ],
                [
                    9,
                    134.09,
                    "TIB"
                ],
                [
                    9,
                    111.43,
                    "TIB"
                ],
                [
                    9,
                    78.58,
                    "TIB"
                ],
                [
                    9,
                    137.55,
                    "TIB"
                ],
                [
                    9,
                    132.22,
                    "TIB"
                ],
                [
                    10,
                    81.59,
                    "BTE"
                ],
                [
                    10,
                    69.1,
                    "BTE"
                ],
                [
                    10,
                    81.26,
                    "BTE"
                ],
                [
                    10,
                    82.52,
                    "BTE"
                ],
                [
                    10,
                    147.85,
                    "BTE"
                ],
                [
                    11,
                    108.2,
                    "EET"
                ],
                [
                    11,
                    67.94,
                    "EET"
                ],
                [
                    11,
                    73.63,
                    "EET"
                ],
                [
                    11,
                    106.06,
                    "EET"
                ],
                [
                    11,
                    105.14,
                    "EET"
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
            "TTC",
            "90s",
            "MMT",
            "ARV",
            "TOM",
            "KTT",
            "RRT",
            "JST",
            "TIB",
            "BTE",
            "EET"
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
                    9
                ],
                [
                    2,
                    0,
                    3
                ],
                [
                    3,
                    0,
                    2
                ],
                [
                    0,
                    1,
                    2
                ],
                [
                    1,
                    1,
                    6
                ],
                [
                    2,
                    1,
                    6
                ],
                [
                    3,
                    1,
                    10
                ],
                [
                    0,
                    2,
                    3
                ],
                [
                    1,
                    2,
                    1
                ],
                [
                    2,
                    2,
                    5
                ],
                [
                    3,
                    2,
                    6
                ],
                [
                    0,
                    3,
                    6
                ],
                [
                    1,
                    3,
                    8
                ],
                [
                    2,
                    3,
                    2
                ],
                [
                    3,
                    3,
                    3
                ],
                [
                    0,
                    4,
                    10
                ],
                [
                    1,
                    4,
                    2
                ],
                [
                    2,
                    4,
                    11
                ],
                [
                    3,
                    4,
                    1
                ],
                [
                    0,
                    5,
                    9
                ],
                [
                    1,
                    5,
                    5
                ],
                [
                    2,
                    5,
                    1
                ],
                [
                    3,
                    5,
                    9
                ],
                [
                    0,
                    6,
                    7
                ],
                [
                    1,
                    6,
                    10
                ],
                [
                    2,
                    6,
                    9
                ],
                [
                    3,
                    6,
                    11
                ],
                [
                    0,
                    7,
                    4
                ],
                [
                    1,
                    7,
                    7
                ],
                [
                    2,
                    7,
                    4
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
                    4
                ],
                [
                    2,
                    8,
                    7
                ],
                [
                    3,
                    8,
                    5
                ],
                [
                    0,
                    9,
                    8
                ],
                [
                    1,
                    9,
                    3
                ],
                [
                    2,
                    9,
                    12
                ],
                [
                    3,
                    9,
                    7
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
                    8
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
                    12
                ],
                [
                    2,
                    11,
                    10
                ],
                [
                    3,
                    11,
                    8
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
            4,
            5
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
            "BTE",
            "TOM",
            "90s",
            "JST",
            "HMB",
            "RRT",
            "MMT",
            "TIB",
            "KTT",
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
                    4,
                    0,
                    6
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
                    2,
                    1,
                    2
                ],
                [
                    3,
                    1,
                    10
                ],
                [
                    4,
                    1,
                    12
                ],
                [
                    0,
                    2,
                    2
                ],
                [
                    1,
                    2,
                    10
                ],
                [
                    2,
                    2,
                    10
                ],
                [
                    3,
                    2,
                    12
                ],
                [
                    4,
                    2,
                    8
                ],
                [
                    0,
                    3,
                    7
                ],
                [
                    1,
                    3,
                    1
                ],
                [
                    2,
                    3,
                    11
                ],
                [
                    3,
                    3,
                    8
                ],
                [
                    4,
                    3,
                    10
                ],
                [
                    0,
                    4,
                    12
                ],
                [
                    1,
                    4,
                    4
                ],
                [
                    2,
                    4,
                    8
                ],
                [
                    3,
                    4,
                    5
                ],
                [
                    4,
                    4,
                    4
                ],
                [
                    0,
                    5,
                    3
                ],
                [
                    1,
                    5,
                    8
                ],
                [
                    2,
                    5,
                    1
                ],
                [
                    3,
                    5,
                    11
                ],
                [
                    4,
                    5,
                    9
                ],
                [
                    0,
                    6,
                    5
                ],
                [
                    1,
                    6,
                    6
                ],
                [
                    2,
                    6,
                    9
                ],
                [
                    3,
                    6,
                    2
                ],
                [
                    4,
                    6,
                    7
                ],
                [
                    0,
                    7,
                    10
                ],
                [
                    1,
                    7,
                    7
                ],
                [
                    2,
                    7,
                    4
                ],
                [
                    3,
                    7,
                    7
                ],
                [
                    4,
                    7,
                    1
                ],
                [
                    0,
                    8,
                    8
                ],
                [
                    1,
                    8,
                    2
                ],
                [
                    2,
                    8,
                    3
                ],
                [
                    3,
                    8,
                    3
                ],
                [
                    4,
                    8,
                    11
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
                    4,
                    9,
                    5
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
                    2,
                    10,
                    7
                ],
                [
                    3,
                    10,
                    6
                ],
                [
                    4,
                    10,
                    2
                ],
                [
                    0,
                    11,
                    9
                ],
                [
                    1,
                    11,
                    3
                ],
                [
                    2,
                    11,
                    5
                ],
                [
                    3,
                    11,
                    1
                ],
                [
                    4,
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
            4,
            5
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
            "HMB",
            "KTT",
            "BTE",
            "MMT",
            "ARV",
            "TIB",
            "JST",
            "TOM",
            "RRT",
            "90s",
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
                    4,
                    0,
                    12
                ],
                [
                    0,
                    1,
                    1
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
                    12
                ],
                [
                    4,
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
                    4,
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
                    12
                ],
                [
                    2,
                    3,
                    4
                ],
                [
                    3,
                    3,
                    6
                ],
                [
                    4,
                    3,
                    5
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
                    4,
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
                    6
                ],
                [
                    2,
                    5,
                    3
                ],
                [
                    3,
                    5,
                    9
                ],
                [
                    4,
                    5,
                    11
                ],
                [
                    0,
                    6,
                    5
                ],
                [
                    1,
                    6,
                    1
                ],
                [
                    2,
                    6,
                    11
                ],
                [
                    3,
                    6,
                    11
                ],
                [
                    4,
                    6,
                    4
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
                    4,
                    7,
                    8
                ],
                [
                    0,
                    8,
                    9
                ],
                [
                    1,
                    8,
                    3
                ],
                [
                    2,
                    8,
                    5
                ],
                [
                    3,
                    8,
                    7
                ],
                [
                    4,
                    8,
                    3
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
                    4,
                    9,
                    6
                ],
                [
                    0,
                    10,
                    4
                ],
                [
                    1,
                    10,
                    8
                ],
                [
                    2,
                    10,
                    1
                ],
                [
                    3,
                    10,
                    1
                ],
                [
                    4,
                    10,
                    2
                ],
                [
                    0,
                    11,
                    1
                ],
                [
                    1,
                    11,
                    7
                ],
                [
                    2,
                    11,
                    2
                ],
                [
                    3,
                    11,
                    4
                ],
                [
                    4,
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
            4,
            5
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
            "TTC",
            "TOM",
            "BTE",
            "KTT",
            "TIB",
            "EET",
            "JST",
            "90s",
            "MMT",
            "HMB",
            "RRT",
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
                    6
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
                    11
                ],
                [
                    4,
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
                    12
                ],
                [
                    2,
                    1,
                    10
                ],
                [
                    3,
                    1,
                    1
                ],
                [
                    4,
                    1,
                    12
                ],
                [
                    0,
                    2,
                    9
                ],
                [
                    1,
                    2,
                    7
                ],
                [
                    2,
                    2,
                    8
                ],
                [
                    3,
                    2,
                    12
                ],
                [
                    4,
                    2,
                    7
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
                    4,
                    3,
                    8
                ],
                [
                    0,
                    4,
                    3
                ],
                [
                    1,
                    4,
                    11
                ],
                [
                    2,
                    4,
                    10
                ],
                [
                    3,
                    4,
                    2
                ],
                [
                    4,
                    4,
                    10
                ],
                [
                    0,
                    5,
                    4
                ],
                [
                    1,
                    5,
                    9
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
                    4,
                    5,
                    9
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
                    4,
                    6,
                    6
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
                    7
                ],
                [
                    3,
                    7,
                    9
                ],
                [
                    4,
                    7,
                    2
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
                    4,
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
                    3
                ],
                [
                    2,
                    9,
                    3
                ],
                [
                    3,
                    9,
                    10
                ],
                [
                    4,
                    9,
                    5
                ],
                [
                    0,
                    10,
                    12
                ],
                [
                    1,
                    10,
                    2
                ],
                [
                    2,
                    10,
                    1
                ],
                [
                    3,
                    10,
                    5
                ],
                [
                    4,
                    10,
                    1
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
                ],
                [
                    4,
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
            4,
            5
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
            "JST",
            "BTE",
            "TTC",
            "MMT",
            "90s",
            "TOM",
            "HMB",
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
                    4,
                    0,
                    8
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
                    4,
                    1,
                    11
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
                    4,
                    2,
                    12
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
                    4,
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
                    4
                ],
                [
                    2,
                    4,
                    11
                ],
                [
                    3,
                    4,
                    6
                ],
                [
                    4,
                    4,
                    10
                ],
                [
                    0,
                    5,
                    6
                ],
                [
                    1,
                    5,
                    7
                ],
                [
                    2,
                    5,
                    4
                ],
                [
                    3,
                    5,
                    10
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    0,
                    6,
                    8
                ],
                [
                    1,
                    6,
                    9
                ],
                [
                    2,
                    6,
                    3
                ],
                [
                    3,
                    6,
                    5
                ],
                [
                    4,
                    6,
                    3
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
                    4,
                    7,
                    1
                ],
                [
                    0,
                    8,
                    1
                ],
                [
                    1,
                    8,
                    5
                ],
                [
                    2,
                    8,
                    5
                ],
                [
                    3,
                    8,
                    7
                ],
                [
                    4,
                    8,
                    5
                ],
                [
                    0,
                    9,
                    2
                ],
                [
                    1,
                    9,
                    3
                ],
                [
                    2,
                    9,
                    9
                ],
                [
                    3,
                    9,
                    1
                ],
                [
                    4,
                    9,
                    7
                ],
                [
                    0,
                    10,
                    7
                ],
                [
                    1,
                    10,
                    1
                ],
                [
                    2,
                    10,
                    8
                ],
                [
                    3,
                    10,
                    4
                ],
                [
                    4,
                    10,
                    2
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
                ],
                [
                    4,
                    11,
                    9
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
            "TTC",
            "90s",
            "MMT",
            "ARV",
            "TOM",
            "KTT",
            "RRT",
            "JST",
            "TIB",
            "BTE",
            "EET"
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
            "Week 4",
            "Week 5"
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
                85.2,
                86.9,
                83.0,
                87.9
            ]
        },
        {
            "name": "TTC",
            "type": "line",
            "data": [
                90.7,
                85.5,
                91.1,
                88.4,
                99.8
            ]
        },
        {
            "name": "90s",
            "type": "line",
            "data": [
                88.5,
                88.3,
                93.2,
                94.2,
                91.9
            ]
        },
        {
            "name": "MMT",
            "type": "line",
            "data": [
                75.5,
                86.5,
                92.7,
                78.0,
                89.2
            ]
        },
        {
            "name": "ARV",
            "type": "line",
            "data": [
                84.2,
                85.0,
                96.4,
                100.0,
                98.2
            ]
        },
        {
            "name": "TOM",
            "type": "line",
            "data": [
                89.1,
                92.5,
                83.6,
                83.3,
                88.2
            ]
        },
        {
            "name": "KTT",
            "type": "line",
            "data": [
                83.0,
                82.6,
                97.1,
                84.6,
                95.1
            ]
        },
        {
            "name": "RRT",
            "type": "line",
            "data": [
                81.4,
                85.3,
                96.9,
                93.0,
                97.2
            ]
        },
        {
            "name": "JST",
            "type": "line",
            "data": [
                91.7,
                95.2,
                88.0,
                83.4,
                100.0
            ]
        },
        {
            "name": "TIB",
            "type": "line",
            "data": [
                79.6,
                77.4,
                68.0,
                77.5,
                98.9
            ]
        },
        {
            "name": "BTE",
            "type": "line",
            "data": [
                77.9,
                74.8,
                79.9,
                76.6,
                100.0
            ]
        },
        {
            "name": "EET",
            "type": "line",
            "data": [
                88.3,
                66.4,
                97.1,
                78.0,
                95.8
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
                        6.0,
                        -1.5,
                        4.8,
                        2.6
                    ],
                    "name": "Game of Zones - House Hamlin"
                }
            ]
        },
        {
            "name": "Third Time's the Charm?",
            "type": "radar",
            "data": [
                {
                    "value": [
                        2.6,
                        -0.0,
                        -3.2,
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
                        4.2,
                        3.8,
                        0.4,
                        2.1
                    ],
                    "name": "90s MonCon"
                }
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        4.3,
                        -0.2,
                        1.6,
                        0.1
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
                        -4.4,
                        3.4,
                        3.5,
                        -5.2
                    ],
                    "name": "Abbey's TNT Team "
                }
            ]
        },
        {
            "name": "Rookie Mistake",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -2.6,
                        1.2,
                        -2.5,
                        3.1
                    ],
                    "name": "Rookie Mistake"
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
                        -2.8,
                        -3.2,
                        -1.6
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
                        -0.9,
                        0.9,
                        0.1,
                        3.0
                    ],
                    "name": "Americas Team "
                }
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "radar",
            "data": [
                {
                    "value": [
                        3.2,
                        2.3,
                        0.8,
                        1.2
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
                        -0.9,
                        1.2,
                        1.2,
                        -5.1
                    ],
                    "name": "To Infinity and Bijan!"
                }
            ]
        },
        {
            "name": "Big Titi Energy",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -6.7,
                        -3.6,
                        -3.9,
                        0.3
                    ],
                    "name": "Big Titi Energy"
                }
            ]
        },
        {
            "name": "Emma's Excellent Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -6.5,
                        -3.0,
                        -0.5,
                        -2.7
                    ],
                    "name": "Emma's Excellent Team"
                }
            ]
        }
    ]
}
```

