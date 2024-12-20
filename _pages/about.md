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

## Welcome to the site for the Family Fantasy Footbal League! We are currently in the 2024-25 season.

<div style="margin-bottom: 30px;">

</div>


The current top scorer is: Kyle Hamlin (1762.02)

The current top scorer is: Abbey Hamlin and Christine Hamlin (1438.72)

Highest Scoring Week: Connor Dickson and Monika Monko - 366.24 points (Week 14)

Lowest Scoring Week: Abbey Hamlin and Christine Hamlin - 73.28 points (Week 7)

Luckiest Team: Cathy Dickson and Jordan Dickson (1.2) Wins Above Expected

Unluckiest Team: Ryan Ratcliff (-3.2) Wins Below Expected


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
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15
        ]
    },
    "yAxis": {
        "type": "value",
        "name": "Rank",
        "nameLocation": "middle",
        "nameGap": 20,
        "inverse": true,
        "min": 1,
        "max": 10
    },
    "series": [
        {
            "name": "Abbey Road to Victory",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#7f7f7f"
            },
            "itemStyle": {
                "color": "#7f7f7f"
            },
            "data": [
                8,
                7,
                8,
                10,
                8,
                8,
                10,
                8,
                8,
                8,
                9,
                8,
                8,
                8,
                8
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Abbey Road t..."
            }
        },
        {
            "name": "Fantasy Guru Kayden",
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
                4,
                8,
                9,
                9,
                9,
                10,
                9,
                9,
                10,
                10,
                10,
                10,
                10,
                9,
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
            "name": "Hamlin My Business ",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#ff7f0e"
            },
            "itemStyle": {
                "color": "#ff7f0e"
            },
            "data": [
                7,
                6,
                4,
                5,
                2,
                1,
                1,
                2,
                3,
                2,
                1,
                2,
                2,
                3,
                3
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Hamlin My Bu..."
            }
        },
        {
            "name": "Hit and Ruggs",
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
                6,
                3,
                2,
                4,
                7,
                7,
                7,
                7,
                6,
                6,
                6,
                6,
                6,
                7,
                7
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Hit and Ruggs"
            }
        },
        {
            "name": "Mama Daughter Duo",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#e377c2"
            },
            "itemStyle": {
                "color": "#e377c2"
            },
            "data": [
                2,
                5,
                6,
                8,
                10,
                9,
                8,
                10,
                9,
                9,
                8,
                7,
                7,
                6,
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
            "name": "Michael's Managable Team",
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
                1,
                4,
                1,
                2,
                3,
                5,
                6,
                5,
                7,
                7,
                7,
                9,
                9,
                10,
                10
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
            "name": "Pink Pony Club",
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
                3,
                2,
                3,
                1,
                1,
                2,
                2,
                1,
                1,
                1,
                2,
                1,
                1,
                1,
                1
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Pink Pony Club"
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
                10,
                9,
                10,
                7,
                6,
                4,
                4,
                3,
                2,
                3,
                4,
                5,
                5,
                5,
                5
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "To Infinity ..."
            }
        },
        {
            "name": "Tom and Jerry",
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
                5,
                1,
                5,
                3,
                5,
                6,
                5,
                6,
                5,
                5,
                5,
                4,
                4,
                4,
                4
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Tom and Jerry"
            }
        },
        {
            "name": "Who Killed Charbonnet Ramsey?",
            "type": "line",
            "smooth": true,
            "lineStyle": {
                "width": 3,
                "color": "#2ca02c"
            },
            "itemStyle": {
                "color": "#2ca02c"
            },
            "data": [
                9,
                10,
                7,
                6,
                4,
                3,
                3,
                4,
                4,
                4,
                3,
                3,
                3,
                2,
                2
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Who Killed C..."
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
        "min": 1479.0,
        "max": 2277.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": 1479.0,
        "max": 2277.0
    },
    "series": [
        {
            "name": "Teams",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                {
                    "name": "Who Killed Charbonnet Ramsey?",
                    "value": [
                        2031.08,
                        1891.3
                    ]
                },
                {
                    "name": "Pink Pony Club",
                    "value": [
                        2126.7,
                        1944.68
                    ]
                },
                {
                    "name": "Tom and Jerry",
                    "value": [
                        1914.84,
                        1889.82
                    ]
                },
                {
                    "name": "Hit and Ruggs",
                    "value": [
                        1900.34,
                        2013.04
                    ]
                },
                {
                    "name": "Michael's Managable Team",
                    "value": [
                        1785.5,
                        1994.16
                    ]
                },
                {
                    "name": "To Infinity and Bijan!",
                    "value": [
                        1769.64,
                        1779.06
                    ]
                },
                {
                    "name": "Fantasy Guru Kayden",
                    "value": [
                        1796.84,
                        1821.64
                    ]
                },
                {
                    "name": "Mama Daughter Duo",
                    "value": [
                        1759.34,
                        1804.56
                    ]
                },
                {
                    "name": "Abbey Road to Victory",
                    "value": [
                        1629.38,
                        1729.52
                    ]
                },
                {
                    "name": "Hamlin My Business ",
                    "value": [
                        2006.4,
                        1852.28
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
                    1479.0,
                    1479.0
                ],
                [
                    2277.0,
                    2277.0
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
                        "xAxis": 1872.01,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 1872.01,
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
            "PONY",
            "HMB",
            "WKCR",
            "TOM",
            "TIB",
            "RRT",
            "JST",
            "ARV",
            "MMT",
            "KTT"
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
                    95.5,
                    127.06,
                    136.96,
                    148.1,
                    179.66
                ],
                [
                    88.18,
                    121.77,
                    135.4,
                    144.16,
                    177.75
                ],
                [
                    47.96,
                    113.64,
                    136.88,
                    157.43,
                    223.12
                ],
                [
                    57.0,
                    107.31,
                    116.56,
                    140.85,
                    191.16
                ],
                [
                    19.06,
                    91.35,
                    120.46,
                    139.54,
                    211.83
                ],
                [
                    62.82,
                    112.97,
                    127.2,
                    146.4,
                    196.54
                ],
                [
                    66.64,
                    106.35,
                    117.3,
                    132.82,
                    172.52
                ],
                [
                    24.16,
                    89.74,
                    98.98,
                    133.46,
                    190.66
                ],
                [
                    52.74,
                    107.31,
                    119.4,
                    143.69,
                    190.2
                ],
                [
                    65.75,
                    103.1,
                    115.94,
                    128.0,
                    165.35
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
                    131.88,
                    "PONY"
                ],
                [
                    0,
                    124.96,
                    "PONY"
                ],
                [
                    0,
                    137.3,
                    "PONY"
                ],
                [
                    0,
                    155.24,
                    "PONY"
                ],
                [
                    0,
                    129.96,
                    "PONY"
                ],
                [
                    0,
                    137.92,
                    "PONY"
                ],
                [
                    0,
                    113.6,
                    "PONY"
                ],
                [
                    0,
                    167.08,
                    "PONY"
                ],
                [
                    0,
                    140.96,
                    "PONY"
                ],
                [
                    0,
                    129.16,
                    "PONY"
                ],
                [
                    0,
                    99.98,
                    "PONY"
                ],
                [
                    0,
                    136.96,
                    "PONY"
                ],
                [
                    0,
                    155.46,
                    "PONY"
                ],
                [
                    0,
                    366.24,
                    "PONY"
                ],
                [
                    0,
                    0.0,
                    "PONY"
                ],
                [
                    1,
                    115.8,
                    "HMB"
                ],
                [
                    1,
                    130.78,
                    "HMB"
                ],
                [
                    1,
                    135.64,
                    "HMB"
                ],
                [
                    1,
                    135.4,
                    "HMB"
                ],
                [
                    1,
                    150.24,
                    "HMB"
                ],
                [
                    1,
                    180.62,
                    "HMB"
                ],
                [
                    1,
                    108.92,
                    "HMB"
                ],
                [
                    1,
                    132.06,
                    "HMB"
                ],
                [
                    1,
                    136.12,
                    "HMB"
                ],
                [
                    1,
                    127.74,
                    "HMB"
                ],
                [
                    1,
                    159.6,
                    "HMB"
                ],
                [
                    1,
                    111.02,
                    "HMB"
                ],
                [
                    1,
                    138.08,
                    "HMB"
                ],
                [
                    1,
                    244.38,
                    "HMB"
                ],
                [
                    1,
                    0.0,
                    "HMB"
                ],
                [
                    2,
                    98.64,
                    "WKCR"
                ],
                [
                    2,
                    82.34,
                    "WKCR"
                ],
                [
                    2,
                    160.06,
                    "WKCR"
                ],
                [
                    2,
                    127.32,
                    "WKCR"
                ],
                [
                    2,
                    173.48,
                    "WKCR"
                ],
                [
                    2,
                    129.96,
                    "WKCR"
                ],
                [
                    2,
                    138.18,
                    "WKCR"
                ],
                [
                    2,
                    118.0,
                    "WKCR"
                ],
                [
                    2,
                    109.28,
                    "WKCR"
                ],
                [
                    2,
                    154.8,
                    "WKCR"
                ],
                [
                    2,
                    145.92,
                    "WKCR"
                ],
                [
                    2,
                    136.88,
                    "WKCR"
                ],
                [
                    2,
                    178.88,
                    "WKCR"
                ],
                [
                    2,
                    277.34,
                    "WKCR"
                ],
                [
                    2,
                    0.0,
                    "WKCR"
                ],
                [
                    3,
                    110.24,
                    "TOM"
                ],
                [
                    3,
                    148.04,
                    "TOM"
                ],
                [
                    3,
                    89.6,
                    "TOM"
                ],
                [
                    3,
                    104.38,
                    "TOM"
                ],
                [
                    3,
                    116.56,
                    "TOM"
                ],
                [
                    3,
                    115.62,
                    "TOM"
                ],
                [
                    3,
                    110.4,
                    "TOM"
                ],
                [
                    3,
                    137.44,
                    "TOM"
                ],
                [
                    3,
                    140.06,
                    "TOM"
                ],
                [
                    3,
                    96.08,
                    "TOM"
                ],
                [
                    3,
                    135.68,
                    "TOM"
                ],
                [
                    3,
                    161.92,
                    "TOM"
                ],
                [
                    3,
                    141.64,
                    "TOM"
                ],
                [
                    3,
                    307.18,
                    "TOM"
                ],
                [
                    3,
                    0.0,
                    "TOM"
                ],
                [
                    4,
                    91.56,
                    "TIB"
                ],
                [
                    4,
                    91.14,
                    "TIB"
                ],
                [
                    4,
                    99.86,
                    "TIB"
                ],
                [
                    4,
                    136.74,
                    "TIB"
                ],
                [
                    4,
                    142.4,
                    "TIB"
                ],
                [
                    4,
                    137.62,
                    "TIB"
                ],
                [
                    4,
                    141.46,
                    "TIB"
                ],
                [
                    4,
                    119.64,
                    "TIB"
                ],
                [
                    4,
                    143.7,
                    "TIB"
                ],
                [
                    4,
                    85.94,
                    "TIB"
                ],
                [
                    4,
                    120.46,
                    "TIB"
                ],
                [
                    4,
                    77.8,
                    "TIB"
                ],
                [
                    4,
                    125.76,
                    "TIB"
                ],
                [
                    4,
                    255.56,
                    "TIB"
                ],
                [
                    4,
                    0.0,
                    "TIB"
                ],
                [
                    5,
                    127.2,
                    "RRT"
                ],
                [
                    5,
                    139.48,
                    "RRT"
                ],
                [
                    5,
                    143.0,
                    "RRT"
                ],
                [
                    5,
                    113.9,
                    "RRT"
                ],
                [
                    5,
                    80.02,
                    "RRT"
                ],
                [
                    5,
                    131.08,
                    "RRT"
                ],
                [
                    5,
                    112.04,
                    "RRT"
                ],
                [
                    5,
                    149.8,
                    "RRT"
                ],
                [
                    5,
                    157.1,
                    "RRT"
                ],
                [
                    5,
                    99.04,
                    "RRT"
                ],
                [
                    5,
                    171.72,
                    "RRT"
                ],
                [
                    5,
                    120.72,
                    "RRT"
                ],
                [
                    5,
                    125.58,
                    "RRT"
                ],
                [
                    5,
                    229.66,
                    "RRT"
                ],
                [
                    5,
                    0.0,
                    "RRT"
                ],
                [
                    6,
                    136.34,
                    "JST"
                ],
                [
                    6,
                    121.86,
                    "JST"
                ],
                [
                    6,
                    104.82,
                    "JST"
                ],
                [
                    6,
                    132.48,
                    "JST"
                ],
                [
                    6,
                    111.32,
                    "JST"
                ],
                [
                    6,
                    90.74,
                    "JST"
                ],
                [
                    6,
                    112.32,
                    "JST"
                ],
                [
                    6,
                    106.68,
                    "JST"
                ],
                [
                    6,
                    133.16,
                    "JST"
                ],
                [
                    6,
                    139.8,
                    "JST"
                ],
                [
                    6,
                    130.16,
                    "JST"
                ],
                [
                    6,
                    117.3,
                    "JST"
                ],
                [
                    6,
                    106.02,
                    "JST"
                ],
                [
                    6,
                    216.34,
                    "JST"
                ],
                [
                    6,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    112.38,
                    "ARV"
                ],
                [
                    7,
                    128.98,
                    "ARV"
                ],
                [
                    7,
                    98.98,
                    "ARV"
                ],
                [
                    7,
                    98.9,
                    "ARV"
                ],
                [
                    7,
                    154.66,
                    "ARV"
                ],
                [
                    7,
                    116.66,
                    "ARV"
                ],
                [
                    7,
                    73.28,
                    "ARV"
                ],
                [
                    7,
                    161.64,
                    "ARV"
                ],
                [
                    7,
                    137.94,
                    "ARV"
                ],
                [
                    7,
                    96.58,
                    "ARV"
                ],
                [
                    7,
                    77.82,
                    "ARV"
                ],
                [
                    7,
                    98.0,
                    "ARV"
                ],
                [
                    7,
                    82.9,
                    "ARV"
                ],
                [
                    7,
                    190.66,
                    "ARV"
                ],
                [
                    7,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    143.22,
                    "MMT"
                ],
                [
                    8,
                    122.86,
                    "MMT"
                ],
                [
                    8,
                    159.98,
                    "MMT"
                ],
                [
                    8,
                    110.14,
                    "MMT"
                ],
                [
                    8,
                    115.48,
                    "MMT"
                ],
                [
                    8,
                    85.74,
                    "MMT"
                ],
                [
                    8,
                    105.82,
                    "MMT"
                ],
                [
                    8,
                    151.72,
                    "MMT"
                ],
                [
                    8,
                    134.62,
                    "MMT"
                ],
                [
                    8,
                    93.36,
                    "MMT"
                ],
                [
                    8,
                    144.16,
                    "MMT"
                ],
                [
                    8,
                    119.4,
                    "MMT"
                ],
                [
                    8,
                    108.8,
                    "MMT"
                ],
                [
                    8,
                    190.2,
                    "MMT"
                ],
                [
                    8,
                    0.0,
                    "MMT"
                ],
                [
                    9,
                    115.94,
                    "KTT"
                ],
                [
                    9,
                    99.9,
                    "KTT"
                ],
                [
                    9,
                    124.42,
                    "KTT"
                ],
                [
                    9,
                    106.3,
                    "KTT"
                ],
                [
                    9,
                    139.88,
                    "KTT"
                ],
                [
                    9,
                    109.68,
                    "KTT"
                ],
                [
                    9,
                    99.26,
                    "KTT"
                ],
                [
                    9,
                    128.52,
                    "KTT"
                ],
                [
                    9,
                    114.92,
                    "KTT"
                ],
                [
                    9,
                    127.48,
                    "KTT"
                ],
                [
                    9,
                    98.46,
                    "KTT"
                ],
                [
                    9,
                    118.04,
                    "KTT"
                ],
                [
                    9,
                    162.8,
                    "KTT"
                ],
                [
                    9,
                    251.24,
                    "KTT"
                ],
                [
                    9,
                    0.0,
                    "KTT"
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
            "PONY",
            "HMB",
            "WKCR",
            "TOM",
            "TIB",
            "RRT",
            "JST",
            "ARV",
            "MMT",
            "KTT"
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
        "max": 10,
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
                    10
                ],
                [
                    3,
                    0,
                    2
                ],
                [
                    0,
                    1,
                    3
                ],
                [
                    1,
                    1,
                    4
                ],
                [
                    2,
                    1,
                    1
                ],
                [
                    3,
                    1,
                    4
                ],
                [
                    0,
                    2,
                    2
                ],
                [
                    1,
                    2,
                    7
                ],
                [
                    2,
                    2,
                    2
                ],
                [
                    3,
                    2,
                    1
                ],
                [
                    0,
                    3,
                    4
                ],
                [
                    1,
                    3,
                    2
                ],
                [
                    2,
                    3,
                    6
                ],
                [
                    3,
                    3,
                    6
                ],
                [
                    0,
                    4,
                    8
                ],
                [
                    1,
                    4,
                    6
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
                    0,
                    5,
                    6
                ],
                [
                    1,
                    5,
                    5
                ],
                [
                    2,
                    5,
                    3
                ],
                [
                    3,
                    5,
                    3
                ],
                [
                    0,
                    6,
                    7
                ],
                [
                    1,
                    6,
                    8
                ],
                [
                    2,
                    6,
                    4
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
                    9
                ],
                [
                    3,
                    7,
                    9
                ],
                [
                    0,
                    8,
                    10
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
                    10
                ],
                [
                    0,
                    9,
                    5
                ],
                [
                    1,
                    9,
                    9
                ],
                [
                    2,
                    9,
                    7
                ],
                [
                    3,
                    9,
                    7
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
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15
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
            "KTT",
            "ARV",
            "RRT",
            "WKCR",
            "MMT",
            "TIB",
            "JST",
            "HMB",
            "TOM",
            "PONY"
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
        "max": 10,
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
                    2
                ],
                [
                    1,
                    0,
                    10
                ],
                [
                    2,
                    0,
                    7
                ],
                [
                    3,
                    0,
                    3
                ],
                [
                    4,
                    0,
                    6
                ],
                [
                    5,
                    0,
                    6
                ],
                [
                    6,
                    0,
                    8
                ],
                [
                    7,
                    0,
                    9
                ],
                [
                    8,
                    0,
                    5
                ],
                [
                    9,
                    0,
                    5
                ],
                [
                    10,
                    0,
                    8
                ],
                [
                    11,
                    0,
                    9
                ],
                [
                    12,
                    0,
                    6
                ],
                [
                    13,
                    0,
                    10
                ],
                [
                    14,
                    0,
                    10
                ],
                [
                    0,
                    1,
                    10
                ],
                [
                    1,
                    1,
                    2
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
                    4,
                    1,
                    1
                ],
                [
                    5,
                    1,
                    8
                ],
                [
                    6,
                    1,
                    7
                ],
                [
                    7,
                    1,
                    2
                ],
                [
                    8,
                    1,
                    6
                ],
                [
                    9,
                    1,
                    4
                ],
                [
                    10,
                    1,
                    10
                ],
                [
                    11,
                    1,
                    10
                ],
                [
                    12,
                    1,
                    10
                ],
                [
                    13,
                    1,
                    9
                ],
                [
                    14,
                    1,
                    6
                ],
                [
                    0,
                    2,
                    4
                ],
                [
                    1,
                    2,
                    8
                ],
                [
                    2,
                    2,
                    4
                ],
                [
                    3,
                    2,
                    4
                ],
                [
                    4,
                    2,
                    10
                ],
                [
                    5,
                    2,
                    9
                ],
                [
                    6,
                    2,
                    4
                ],
                [
                    7,
                    2,
                    7
                ],
                [
                    8,
                    2,
                    4
                ],
                [
                    9,
                    2,
                    8
                ],
                [
                    10,
                    2,
                    3
                ],
                [
                    11,
                    2,
                    8
                ],
                [
                    12,
                    2,
                    7
                ],
                [
                    13,
                    2,
                    7
                ],
                [
                    14,
                    2,
                    7
                ],
                [
                    0,
                    3,
                    9
                ],
                [
                    1,
                    3,
                    9
                ],
                [
                    2,
                    3,
                    10
                ],
                [
                    3,
                    3,
                    8
                ],
                [
                    4,
                    3,
                    2
                ],
                [
                    5,
                    3,
                    1
                ],
                [
                    6,
                    3,
                    2
                ],
                [
                    7,
                    3,
                    10
                ],
                [
                    8,
                    3,
                    10
                ],
                [
                    9,
                    3,
                    9
                ],
                [
                    10,
                    3,
                    6
                ],
                [
                    11,
                    3,
                    2
                ],
                [
                    12,
                    3,
                    3
                ],
                [
                    13,
                    3,
                    1
                ],
                [
                    14,
                    3,
                    9
                ],
                [
                    0,
                    4,
                    6
                ],
                [
                    1,
                    4,
                    3
                ],
                [
                    2,
                    4,
                    1
                ],
                [
                    3,
                    4,
                    5
                ],
                [
                    4,
                    4,
                    9
                ],
                [
                    5,
                    4,
                    10
                ],
                [
                    6,
                    4,
                    10
                ],
                [
                    7,
                    4,
                    8
                ],
                [
                    8,
                    4,
                    8
                ],
                [
                    9,
                    4,
                    3
                ],
                [
                    10,
                    4,
                    2
                ],
                [
                    11,
                    4,
                    5
                ],
                [
                    12,
                    4,
                    9
                ],
                [
                    13,
                    4,
                    6
                ],
                [
                    14,
                    4,
                    4
                ],
                [
                    0,
                    5,
                    5
                ],
                [
                    1,
                    5,
                    6
                ],
                [
                    2,
                    5,
                    8
                ],
                [
                    3,
                    5,
                    6
                ],
                [
                    4,
                    5,
                    5
                ],
                [
                    5,
                    5,
                    7
                ],
                [
                    6,
                    5,
                    5
                ],
                [
                    7,
                    5,
                    4
                ],
                [
                    8,
                    5,
                    2
                ],
                [
                    9,
                    5,
                    10
                ],
                [
                    10,
                    5,
                    9
                ],
                [
                    11,
                    5,
                    6
                ],
                [
                    12,
                    5,
                    2
                ],
                [
                    13,
                    5,
                    4
                ],
                [
                    14,
                    5,
                    5
                ],
                [
                    0,
                    6,
                    7
                ],
                [
                    1,
                    6,
                    7
                ],
                [
                    2,
                    6,
                    5
                ],
                [
                    3,
                    6,
                    9
                ],
                [
                    4,
                    6,
                    4
                ],
                [
                    5,
                    6,
                    5
                ],
                [
                    6,
                    6,
                    6
                ],
                [
                    7,
                    6,
                    1
                ],
                [
                    8,
                    6,
                    7
                ],
                [
                    9,
                    6,
                    2
                ],
                [
                    10,
                    6,
                    1
                ],
                [
                    11,
                    6,
                    7
                ],
                [
                    12,
                    6,
                    4
                ],
                [
                    13,
                    6,
                    8
                ],
                [
                    14,
                    6,
                    3
                ],
                [
                    0,
                    7,
                    8
                ],
                [
                    1,
                    7,
                    4
                ],
                [
                    2,
                    7,
                    3
                ],
                [
                    3,
                    7,
                    7
                ],
                [
                    4,
                    7,
                    8
                ],
                [
                    5,
                    7,
                    3
                ],
                [
                    6,
                    7,
                    3
                ],
                [
                    7,
                    7,
                    3
                ],
                [
                    8,
                    7,
                    3
                ],
                [
                    9,
                    7,
                    1
                ],
                [
                    10,
                    7,
                    5
                ],
                [
                    11,
                    7,
                    3
                ],
                [
                    12,
                    7,
                    5
                ],
                [
                    13,
                    7,
                    2
                ],
                [
                    14,
                    7,
                    8
                ],
                [
                    0,
                    8,
                    3
                ],
                [
                    1,
                    8,
                    1
                ],
                [
                    2,
                    8,
                    9
                ],
                [
                    3,
                    8,
                    1
                ],
                [
                    4,
                    8,
                    3
                ],
                [
                    5,
                    8,
                    2
                ],
                [
                    6,
                    8,
                    1
                ],
                [
                    7,
                    8,
                    5
                ],
                [
                    8,
                    8,
                    9
                ],
                [
                    9,
                    8,
                    6
                ],
                [
                    10,
                    8,
                    4
                ],
                [
                    11,
                    8,
                    4
                ],
                [
                    12,
                    8,
                    8
                ],
                [
                    13,
                    8,
                    3
                ],
                [
                    14,
                    8,
                    1
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
                    2
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
                    5,
                    9,
                    4
                ],
                [
                    6,
                    9,
                    9
                ],
                [
                    7,
                    9,
                    6
                ],
                [
                    8,
                    9,
                    1
                ],
                [
                    9,
                    9,
                    7
                ],
                [
                    10,
                    9,
                    7
                ],
                [
                    11,
                    9,
                    1
                ],
                [
                    12,
                    9,
                    1
                ],
                [
                    13,
                    9,
                    5
                ],
                [
                    14,
                    9,
                    2
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
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15
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
            "WKCR",
            "TIB",
            "TOM",
            "RRT",
            "MMT",
            "ARV",
            "HMB",
            "JST",
            "KTT",
            "PONY"
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
        "max": 10,
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
                    7
                ],
                [
                    1,
                    0,
                    9
                ],
                [
                    2,
                    0,
                    10
                ],
                [
                    3,
                    0,
                    5
                ],
                [
                    4,
                    0,
                    7
                ],
                [
                    5,
                    0,
                    6
                ],
                [
                    6,
                    0,
                    7
                ],
                [
                    7,
                    0,
                    8
                ],
                [
                    8,
                    0,
                    6
                ],
                [
                    9,
                    0,
                    7
                ],
                [
                    10,
                    0,
                    9
                ],
                [
                    11,
                    0,
                    10
                ],
                [
                    12,
                    0,
                    2
                ],
                [
                    13,
                    0,
                    5
                ],
                [
                    14,
                    0,
                    8
                ],
                [
                    0,
                    1,
                    9
                ],
                [
                    1,
                    1,
                    6
                ],
                [
                    2,
                    1,
                    3
                ],
                [
                    3,
                    1,
                    10
                ],
                [
                    4,
                    1,
                    4
                ],
                [
                    5,
                    1,
                    3
                ],
                [
                    6,
                    1,
                    2
                ],
                [
                    7,
                    1,
                    7
                ],
                [
                    8,
                    1,
                    7
                ],
                [
                    9,
                    1,
                    9
                ],
                [
                    10,
                    1,
                    3
                ],
                [
                    11,
                    1,
                    5
                ],
                [
                    12,
                    1,
                    7
                ],
                [
                    13,
                    1,
                    9
                ],
                [
                    14,
                    1,
                    7
                ],
                [
                    0,
                    2,
                    8
                ],
                [
                    1,
                    2,
                    10
                ],
                [
                    2,
                    2,
                    4
                ],
                [
                    3,
                    2,
                    6
                ],
                [
                    4,
                    2,
                    10
                ],
                [
                    5,
                    2,
                    5
                ],
                [
                    6,
                    2,
                    10
                ],
                [
                    7,
                    2,
                    6
                ],
                [
                    8,
                    2,
                    4
                ],
                [
                    9,
                    2,
                    10
                ],
                [
                    10,
                    2,
                    2
                ],
                [
                    11,
                    2,
                    8
                ],
                [
                    12,
                    2,
                    3
                ],
                [
                    13,
                    2,
                    2
                ],
                [
                    14,
                    2,
                    1
                ],
                [
                    0,
                    3,
                    3
                ],
                [
                    1,
                    3,
                    1
                ],
                [
                    2,
                    3,
                    8
                ],
                [
                    3,
                    3,
                    9
                ],
                [
                    4,
                    3,
                    9
                ],
                [
                    5,
                    3,
                    8
                ],
                [
                    6,
                    3,
                    6
                ],
                [
                    7,
                    3,
                    5
                ],
                [
                    8,
                    3,
                    1
                ],
                [
                    9,
                    3,
                    2
                ],
                [
                    10,
                    3,
                    10
                ],
                [
                    11,
                    3,
                    7
                ],
                [
                    12,
                    3,
                    5
                ],
                [
                    13,
                    3,
                    10
                ],
                [
                    14,
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
                    3
                ],
                [
                    2,
                    4,
                    9
                ],
                [
                    3,
                    4,
                    8
                ],
                [
                    4,
                    4,
                    2
                ],
                [
                    5,
                    4,
                    7
                ],
                [
                    6,
                    4,
                    5
                ],
                [
                    7,
                    4,
                    2
                ],
                [
                    8,
                    4,
                    2
                ],
                [
                    9,
                    4,
                    8
                ],
                [
                    10,
                    4,
                    1
                ],
                [
                    11,
                    4,
                    9
                ],
                [
                    12,
                    4,
                    10
                ],
                [
                    13,
                    4,
                    8
                ],
                [
                    14,
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
                    4
                ],
                [
                    2,
                    5,
                    2
                ],
                [
                    3,
                    5,
                    4
                ],
                [
                    4,
                    5,
                    5
                ],
                [
                    5,
                    5,
                    4
                ],
                [
                    6,
                    5,
                    4
                ],
                [
                    7,
                    5,
                    9
                ],
                [
                    8,
                    5,
                    9
                ],
                [
                    9,
                    5,
                    6
                ],
                [
                    10,
                    5,
                    7
                ],
                [
                    11,
                    5,
                    1
                ],
                [
                    12,
                    5,
                    8
                ],
                [
                    13,
                    5,
                    6
                ],
                [
                    14,
                    5,
                    9
                ],
                [
                    0,
                    6,
                    10
                ],
                [
                    1,
                    6,
                    7
                ],
                [
                    2,
                    6,
                    1
                ],
                [
                    3,
                    6,
                    7
                ],
                [
                    4,
                    6,
                    8
                ],
                [
                    5,
                    6,
                    2
                ],
                [
                    6,
                    6,
                    9
                ],
                [
                    7,
                    6,
                    1
                ],
                [
                    8,
                    6,
                    5
                ],
                [
                    9,
                    6,
                    5
                ],
                [
                    10,
                    6,
                    8
                ],
                [
                    11,
                    6,
                    2
                ],
                [
                    12,
                    6,
                    6
                ],
                [
                    13,
                    6,
                    4
                ],
                [
                    14,
                    6,
                    2
                ],
                [
                    0,
                    7,
                    1
                ],
                [
                    1,
                    7,
                    2
                ],
                [
                    2,
                    7,
                    6
                ],
                [
                    3,
                    7,
                    1
                ],
                [
                    4,
                    7,
                    6
                ],
                [
                    5,
                    7,
                    9
                ],
                [
                    6,
                    7,
                    1
                ],
                [
                    7,
                    7,
                    10
                ],
                [
                    8,
                    7,
                    10
                ],
                [
                    9,
                    7,
                    1
                ],
                [
                    10,
                    7,
                    4
                ],
                [
                    11,
                    7,
                    3
                ],
                [
                    12,
                    7,
                    9
                ],
                [
                    13,
                    7,
                    3
                ],
                [
                    14,
                    7,
                    5
                ],
                [
                    0,
                    8,
                    5
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
                    2
                ],
                [
                    4,
                    8,
                    1
                ],
                [
                    5,
                    8,
                    10
                ],
                [
                    6,
                    8,
                    8
                ],
                [
                    7,
                    8,
                    4
                ],
                [
                    8,
                    8,
                    3
                ],
                [
                    9,
                    8,
                    4
                ],
                [
                    10,
                    8,
                    6
                ],
                [
                    11,
                    8,
                    4
                ],
                [
                    12,
                    8,
                    1
                ],
                [
                    13,
                    8,
                    7
                ],
                [
                    14,
                    8,
                    6
                ],
                [
                    0,
                    9,
                    4
                ],
                [
                    1,
                    9,
                    8
                ],
                [
                    2,
                    9,
                    7
                ],
                [
                    3,
                    9,
                    3
                ],
                [
                    4,
                    9,
                    3
                ],
                [
                    5,
                    9,
                    1
                ],
                [
                    6,
                    9,
                    3
                ],
                [
                    7,
                    9,
                    3
                ],
                [
                    8,
                    9,
                    8
                ],
                [
                    9,
                    9,
                    3
                ],
                [
                    10,
                    9,
                    5
                ],
                [
                    11,
                    9,
                    6
                ],
                [
                    12,
                    9,
                    4
                ],
                [
                    13,
                    9,
                    1
                ],
                [
                    14,
                    9,
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
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15
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
            "MMT",
            "TOM",
            "WKCR",
            "ARV",
            "HMB",
            "TIB",
            "KTT",
            "RRT",
            "PONY",
            "JST"
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
        "max": 10,
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
                    5
                ],
                [
                    2,
                    0,
                    1
                ],
                [
                    3,
                    0,
                    6
                ],
                [
                    4,
                    0,
                    9
                ],
                [
                    5,
                    0,
                    6
                ],
                [
                    6,
                    0,
                    7
                ],
                [
                    7,
                    0,
                    9
                ],
                [
                    8,
                    0,
                    6
                ],
                [
                    9,
                    0,
                    5
                ],
                [
                    10,
                    0,
                    5
                ],
                [
                    11,
                    0,
                    6
                ],
                [
                    12,
                    0,
                    6
                ],
                [
                    13,
                    0,
                    9
                ],
                [
                    14,
                    0,
                    8
                ],
                [
                    0,
                    1,
                    4
                ],
                [
                    1,
                    1,
                    1
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
                    10
                ],
                [
                    5,
                    1,
                    10
                ],
                [
                    6,
                    1,
                    5
                ],
                [
                    7,
                    1,
                    4
                ],
                [
                    8,
                    1,
                    10
                ],
                [
                    9,
                    1,
                    7
                ],
                [
                    10,
                    1,
                    6
                ],
                [
                    11,
                    1,
                    7
                ],
                [
                    12,
                    1,
                    8
                ],
                [
                    13,
                    1,
                    2
                ],
                [
                    14,
                    1,
                    7
                ],
                [
                    0,
                    2,
                    7
                ],
                [
                    1,
                    2,
                    9
                ],
                [
                    2,
                    2,
                    3
                ],
                [
                    3,
                    2,
                    7
                ],
                [
                    4,
                    2,
                    5
                ],
                [
                    5,
                    2,
                    1
                ],
                [
                    6,
                    2,
                    6
                ],
                [
                    7,
                    2,
                    6
                ],
                [
                    8,
                    2,
                    7
                ],
                [
                    9,
                    2,
                    10
                ],
                [
                    10,
                    2,
                    2
                ],
                [
                    11,
                    2,
                    8
                ],
                [
                    12,
                    2,
                    9
                ],
                [
                    13,
                    2,
                    6
                ],
                [
                    14,
                    2,
                    9
                ],
                [
                    0,
                    3,
                    5
                ],
                [
                    1,
                    3,
                    9
                ],
                [
                    2,
                    3,
                    5
                ],
                [
                    3,
                    3,
                    10
                ],
                [
                    4,
                    3,
                    8
                ],
                [
                    5,
                    3,
                    9
                ],
                [
                    6,
                    3,
                    4
                ],
                [
                    7,
                    3,
                    1
                ],
                [
                    8,
                    3,
                    1
                ],
                [
                    9,
                    3,
                    9
                ],
                [
                    10,
                    3,
                    9
                ],
                [
                    11,
                    3,
                    9
                ],
                [
                    12,
                    3,
                    4
                ],
                [
                    13,
                    3,
                    7
                ],
                [
                    14,
                    3,
                    5
                ],
                [
                    0,
                    4,
                    2
                ],
                [
                    1,
                    4,
                    2
                ],
                [
                    2,
                    4,
                    10
                ],
                [
                    3,
                    4,
                    1
                ],
                [
                    4,
                    4,
                    1
                ],
                [
                    5,
                    4,
                    3
                ],
                [
                    6,
                    4,
                    9
                ],
                [
                    7,
                    4,
                    10
                ],
                [
                    8,
                    4,
                    9
                ],
                [
                    9,
                    4,
                    6
                ],
                [
                    10,
                    4,
                    8
                ],
                [
                    11,
                    4,
                    5
                ],
                [
                    12,
                    4,
                    5
                ],
                [
                    13,
                    4,
                    10
                ],
                [
                    14,
                    4,
                    4
                ],
                [
                    0,
                    5,
                    6
                ],
                [
                    1,
                    5,
                    6
                ],
                [
                    2,
                    5,
                    9
                ],
                [
                    3,
                    5,
                    3
                ],
                [
                    4,
                    5,
                    3
                ],
                [
                    5,
                    5,
                    4
                ],
                [
                    6,
                    5,
                    8
                ],
                [
                    7,
                    5,
                    8
                ],
                [
                    8,
                    5,
                    4
                ],
                [
                    9,
                    5,
                    3
                ],
                [
                    10,
                    5,
                    3
                ],
                [
                    11,
                    5,
                    10
                ],
                [
                    12,
                    5,
                    10
                ],
                [
                    13,
                    5,
                    5
                ],
                [
                    14,
                    5,
                    2
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
                    4
                ],
                [
                    3,
                    6,
                    5
                ],
                [
                    4,
                    6,
                    6
                ],
                [
                    5,
                    6,
                    7
                ],
                [
                    6,
                    6,
                    10
                ],
                [
                    7,
                    6,
                    5
                ],
                [
                    8,
                    6,
                    3
                ],
                [
                    9,
                    6,
                    4
                ],
                [
                    10,
                    6,
                    10
                ],
                [
                    11,
                    6,
                    4
                ],
                [
                    12,
                    6,
                    3
                ],
                [
                    13,
                    6,
                    8
                ],
                [
                    14,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    8
                ],
                [
                    1,
                    7,
                    7
                ],
                [
                    2,
                    7,
                    2
                ],
                [
                    3,
                    7,
                    9
                ],
                [
                    4,
                    7,
                    4
                ],
                [
                    5,
                    7,
                    5
                ],
                [
                    6,
                    7,
                    3
                ],
                [
                    7,
                    7,
                    2
                ],
                [
                    8,
                    7,
                    2
                ],
                [
                    9,
                    7,
                    2
                ],
                [
                    10,
                    7,
                    1
                ],
                [
                    11,
                    7,
                    3
                ],
                [
                    12,
                    7,
                    7
                ],
                [
                    13,
                    7,
                    4
                ],
                [
                    14,
                    7,
                    9
                ],
                [
                    0,
                    8,
                    9
                ],
                [
                    1,
                    8,
                    8
                ],
                [
                    2,
                    8,
                    6
                ],
                [
                    3,
                    8,
                    4
                ],
                [
                    4,
                    8,
                    2
                ],
                [
                    5,
                    8,
                    8
                ],
                [
                    6,
                    8,
                    1
                ],
                [
                    7,
                    8,
                    3
                ],
                [
                    8,
                    8,
                    8
                ],
                [
                    9,
                    8,
                    1
                ],
                [
                    10,
                    8,
                    7
                ],
                [
                    11,
                    8,
                    2
                ],
                [
                    12,
                    8,
                    1
                ],
                [
                    13,
                    8,
                    3
                ],
                [
                    14,
                    8,
                    1
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
                    8
                ],
                [
                    3,
                    9,
                    2
                ],
                [
                    4,
                    9,
                    7
                ],
                [
                    5,
                    9,
                    2
                ],
                [
                    6,
                    9,
                    2
                ],
                [
                    7,
                    9,
                    7
                ],
                [
                    8,
                    9,
                    5
                ],
                [
                    9,
                    9,
                    8
                ],
                [
                    10,
                    9,
                    4
                ],
                [
                    11,
                    9,
                    1
                ],
                [
                    12,
                    9,
                    2
                ],
                [
                    13,
                    9,
                    1
                ],
                [
                    14,
                    9,
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
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15
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
            "PONY",
            "TOM",
            "ARV",
            "TIB",
            "MMT",
            "KTT",
            "RRT",
            "WKCR",
            "JST",
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
        "max": 10,
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
                    7
                ],
                [
                    1,
                    0,
                    9
                ],
                [
                    2,
                    0,
                    2
                ],
                [
                    3,
                    0,
                    5
                ],
                [
                    4,
                    0,
                    6
                ],
                [
                    5,
                    0,
                    7
                ],
                [
                    6,
                    0,
                    9
                ],
                [
                    7,
                    0,
                    10
                ],
                [
                    8,
                    0,
                    5
                ],
                [
                    9,
                    0,
                    7
                ],
                [
                    10,
                    0,
                    5
                ],
                [
                    11,
                    0,
                    8
                ],
                [
                    12,
                    0,
                    9
                ],
                [
                    13,
                    0,
                    4
                ],
                [
                    14,
                    0,
                    7
                ],
                [
                    0,
                    1,
                    10
                ],
                [
                    1,
                    1,
                    6
                ],
                [
                    2,
                    1,
                    9
                ],
                [
                    3,
                    1,
                    8
                ],
                [
                    4,
                    1,
                    1
                ],
                [
                    5,
                    1,
                    9
                ],
                [
                    6,
                    1,
                    6
                ],
                [
                    7,
                    1,
                    5
                ],
                [
                    8,
                    1,
                    7
                ],
                [
                    9,
                    1,
                    10
                ],
                [
                    10,
                    1,
                    9
                ],
                [
                    11,
                    1,
                    1
                ],
                [
                    12,
                    1,
                    3
                ],
                [
                    13,
                    1,
                    3
                ],
                [
                    14,
                    1,
                    1
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
                    2,
                    2,
                    8
                ],
                [
                    3,
                    2,
                    3
                ],
                [
                    4,
                    2,
                    5
                ],
                [
                    5,
                    2,
                    10
                ],
                [
                    6,
                    2,
                    10
                ],
                [
                    7,
                    2,
                    3
                ],
                [
                    8,
                    2,
                    2
                ],
                [
                    9,
                    2,
                    1
                ],
                [
                    10,
                    2,
                    7
                ],
                [
                    11,
                    2,
                    4
                ],
                [
                    12,
                    2,
                    6
                ],
                [
                    13,
                    2,
                    6
                ],
                [
                    14,
                    2,
                    6
                ],
                [
                    0,
                    3,
                    9
                ],
                [
                    1,
                    3,
                    5
                ],
                [
                    2,
                    3,
                    3
                ],
                [
                    3,
                    3,
                    6
                ],
                [
                    4,
                    3,
                    9
                ],
                [
                    5,
                    3,
                    1
                ],
                [
                    6,
                    3,
                    4
                ],
                [
                    7,
                    3,
                    1
                ],
                [
                    8,
                    3,
                    1
                ],
                [
                    9,
                    3,
                    7
                ],
                [
                    10,
                    3,
                    9
                ],
                [
                    11,
                    3,
                    3
                ],
                [
                    12,
                    3,
                    8
                ],
                [
                    13,
                    3,
                    9
                ],
                [
                    14,
                    3,
                    8
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
                    6
                ],
                [
                    3,
                    4,
                    7
                ],
                [
                    4,
                    4,
                    2
                ],
                [
                    5,
                    4,
                    5
                ],
                [
                    6,
                    4,
                    3
                ],
                [
                    7,
                    4,
                    8
                ],
                [
                    8,
                    4,
                    9
                ],
                [
                    9,
                    4,
                    3
                ],
                [
                    10,
                    4,
                    9
                ],
                [
                    11,
                    4,
                    9
                ],
                [
                    12,
                    4,
                    4
                ],
                [
                    13,
                    4,
                    5
                ],
                [
                    14,
                    4,
                    2
                ],
                [
                    0,
                    5,
                    1
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
                    9
                ],
                [
                    4,
                    5,
                    4
                ],
                [
                    5,
                    5,
                    6
                ],
                [
                    6,
                    5,
                    7
                ],
                [
                    7,
                    5,
                    2
                ],
                [
                    8,
                    5,
                    10
                ],
                [
                    9,
                    5,
                    4
                ],
                [
                    10,
                    5,
                    6
                ],
                [
                    11,
                    5,
                    2
                ],
                [
                    12,
                    5,
                    7
                ],
                [
                    13,
                    5,
                    8
                ],
                [
                    14,
                    5,
                    4
                ],
                [
                    0,
                    6,
                    5
                ],
                [
                    1,
                    6,
                    2
                ],
                [
                    2,
                    6,
                    1
                ],
                [
                    3,
                    6,
                    4
                ],
                [
                    4,
                    6,
                    7
                ],
                [
                    5,
                    6,
                    4
                ],
                [
                    6,
                    6,
                    8
                ],
                [
                    7,
                    6,
                    4
                ],
                [
                    8,
                    6,
                    4
                ],
                [
                    9,
                    6,
                    6
                ],
                [
                    10,
                    6,
                    4
                ],
                [
                    11,
                    6,
                    7
                ],
                [
                    12,
                    6,
                    5
                ],
                [
                    13,
                    6,
                    9
                ],
                [
                    14,
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
                    3
                ],
                [
                    2,
                    7,
                    10
                ],
                [
                    3,
                    7,
                    10
                ],
                [
                    4,
                    7,
                    10
                ],
                [
                    5,
                    7,
                    3
                ],
                [
                    6,
                    7,
                    2
                ],
                [
                    7,
                    7,
                    7
                ],
                [
                    8,
                    7,
                    3
                ],
                [
                    9,
                    7,
                    2
                ],
                [
                    10,
                    7,
                    1
                ],
                [
                    11,
                    7,
                    6
                ],
                [
                    12,
                    7,
                    1
                ],
                [
                    13,
                    7,
                    7
                ],
                [
                    14,
                    7,
                    5
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
                    2,
                    8,
                    7
                ],
                [
                    3,
                    8,
                    1
                ],
                [
                    4,
                    8,
                    8
                ],
                [
                    5,
                    8,
                    7
                ],
                [
                    6,
                    8,
                    1
                ],
                [
                    7,
                    8,
                    6
                ],
                [
                    8,
                    8,
                    8
                ],
                [
                    9,
                    8,
                    5
                ],
                [
                    10,
                    8,
                    2
                ],
                [
                    11,
                    8,
                    9
                ],
                [
                    12,
                    8,
                    2
                ],
                [
                    13,
                    8,
                    2
                ],
                [
                    14,
                    8,
                    9
                ],
                [
                    0,
                    9,
                    4
                ],
                [
                    1,
                    9,
                    1
                ],
                [
                    2,
                    9,
                    5
                ],
                [
                    3,
                    9,
                    2
                ],
                [
                    4,
                    9,
                    3
                ],
                [
                    5,
                    9,
                    2
                ],
                [
                    6,
                    9,
                    5
                ],
                [
                    7,
                    9,
                    9
                ],
                [
                    8,
                    9,
                    6
                ],
                [
                    9,
                    9,
                    9
                ],
                [
                    10,
                    9,
                    3
                ],
                [
                    11,
                    9,
                    5
                ],
                [
                    12,
                    9,
                    10
                ],
                [
                    13,
                    9,
                    1
                ],
                [
                    14,
                    9,
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
            "PONY",
            "HMB",
            "WKCR",
            "TOM",
            "TIB",
            "RRT",
            "JST",
            "ARV",
            "MMT",
            "KTT"
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
            "Week 5",
            "Week 6",
            "Week 7",
            "Week 8",
            "Week 9",
            "Week 10",
            "Week 11",
            "Week 12",
            "Week 13",
            "Week 14",
            "Week 15"
        ]
    },
    "yAxis": {
        "type": "value",
        "name": "Efficiency %"
    },
    "series": [
        {
            "name": "PONY",
            "type": "line",
            "data": [
                87.3,
                92.7,
                68.3,
                88.1,
                89.6,
                89.9,
                69.3,
                91.6,
                96.7,
                87.1,
                86.5,
                93.9,
                81.6,
                93.5,
                93.9
            ]
        },
        {
            "name": "HMB",
            "type": "line",
            "data": [
                79.7,
                90.9,
                90.1,
                93.8,
                95.9,
                88.7,
                78.5,
                73.0,
                95.6,
                93.9,
                90.1,
                87.2,
                84.9,
                96.8,
                77.5
            ]
        },
        {
            "name": "WKCR",
            "type": "line",
            "data": [
                92.0,
                71.7,
                90.0,
                80.3,
                89.5,
                78.3,
                85.6,
                81.2,
                86.1,
                93.3,
                90.3,
                99.9,
                97.2,
                90.8,
                69.6
            ]
        },
        {
            "name": "TOM",
            "type": "line",
            "data": [
                80.1,
                96.2,
                88.5,
                71.8,
                77.9,
                85.1,
                89.5,
                89.5,
                87.1,
                85.6,
                77.0,
                92.6,
                88.6,
                99.7,
                85.5
            ]
        },
        {
            "name": "TIB",
            "type": "line",
            "data": [
                77.4,
                72.3,
                73.0,
                93.2,
                87.1,
                83.6,
                95.9,
                79.2,
                88.8,
                95.9,
                89.1,
                95.0,
                93.3,
                96.4,
                88.6
            ]
        },
        {
            "name": "RRT",
            "type": "line",
            "data": [
                90.4,
                88.3,
                83.5,
                73.7,
                75.8,
                96.3,
                95.2,
                98.2,
                88.8,
                95.7,
                95.1,
                88.1,
                84.1,
                67.3,
                65.1
            ]
        },
        {
            "name": "JST",
            "type": "line",
            "data": [
                95.7,
                91.3,
                85.5,
                84.0,
                94.8,
                80.8,
                79.0,
                75.1,
                83.5,
                100.0,
                88.7,
                74.6,
                67.2,
                75.5,
                72.5
            ]
        },
        {
            "name": "ARV",
            "type": "line",
            "data": [
                87.0,
                88.4,
                90.8,
                76.3,
                97.6,
                86.4,
                84.2,
                99.0,
                88.3,
                87.9,
                55.3,
                100.0,
                86.0,
                88.8,
                76.6
            ]
        },
        {
            "name": "MMT",
            "type": "line",
            "data": [
                90.0,
                79.4,
                90.8,
                74.7,
                100.0,
                82.4,
                88.1,
                90.4,
                89.9,
                96.9,
                100.0,
                90.8,
                94.4,
                72.5,
                85.9
            ]
        },
        {
            "name": "KTT",
            "type": "line",
            "data": [
                91.8,
                84.1,
                80.4,
                89.4,
                100.0,
                100.0,
                75.9,
                83.7,
                78.6,
                98.9,
                83.6,
                91.8,
                96.0,
                93.7,
                80.7
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
            "name": "Pink Pony Club",
            "type": "radar",
            "data": [
                {
                    "value": [
                        3.4,
                        1.7,
                        0.3,
                        -2.6
                    ],
                    "name": "Pink Pony Club"
                }
            ]
        },
        {
            "name": "Hamlin My Business ",
            "type": "radar",
            "data": [
                {
                    "value": [
                        2.1,
                        -0.6,
                        1.3,
                        3.2
                    ],
                    "name": "Hamlin My Business "
                }
            ]
        },
        {
            "name": "Who Killed Charbonnet Ramsey?",
            "type": "radar",
            "data": [
                {
                    "value": [
                        2.3,
                        0.3,
                        0.4,
                        -0.1
                    ],
                    "name": "Who Killed Charbonnet Ramsey?"
                }
            ]
        },
        {
            "name": "Tom and Jerry",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.7,
                        0.7,
                        -1.0,
                        -1.8
                    ],
                    "name": "Tom and Jerry"
                }
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -2.3,
                        -0.1,
                        -0.5,
                        0.5
                    ],
                    "name": "To Infinity and Bijan!"
                }
            ]
        },
        {
            "name": "Hit and Ruggs",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -1.1,
                        -0.2,
                        1.0,
                        2.4
                    ],
                    "name": "Hit and Ruggs"
                }
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -1.4,
                        -1.1,
                        -0.0,
                        0.5
                    ],
                    "name": "Mama Daughter Duo"
                }
            ]
        },
        {
            "name": "Abbey Road to Victory",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -1.4,
                        -1.8,
                        -0.2,
                        -1.2
                    ],
                    "name": "Abbey Road to Victory"
                }
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -3.5,
                        1.6,
                        -0.3,
                        -0.8
                    ],
                    "name": "Michael's Managable Team"
                }
            ]
        },
        {
            "name": "Fantasy Guru Kayden",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.2,
                        -1.4,
                        -0.9,
                        -0.5
                    ],
                    "name": "Fantasy Guru Kayden"
                }
            ]
        }
    ]
}
```

