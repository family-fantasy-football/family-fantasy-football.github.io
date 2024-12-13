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

Highest Scoring Week: Kyle Hamlin - 180.62 points (Week 6)

Lowest Scoring Week: Michael Ratcliff - 72.52 points (Week 14)

Luckiest Team: Nick Hill (1.3) Wins Above Expected

Unluckiest Team: Ryan Ratcliff (-2.9) Wins Below Expected


### Current Standings:

<table
    data-click-to-select="true"
    data-height="635"
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
            14
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
                6
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
                7
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
                9
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
        "min": 1397.0,
        "max": 2080.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": 1397.0,
        "max": 2080.0
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
                        1922.04,
                        1791.28
                    ]
                },
                {
                    "name": "Pink Pony Club",
                    "value": [
                        1929.66,
                        1791.9
                    ]
                },
                {
                    "name": "Tom and Jerry",
                    "value": [
                        1762.06,
                        1692.78
                    ]
                },
                {
                    "name": "Hit and Ruggs",
                    "value": [
                        1802.12,
                        1861.46
                    ]
                },
                {
                    "name": "Michael's Managable Team",
                    "value": [
                        1667.82,
                        1866.32
                    ]
                },
                {
                    "name": "To Infinity and Bijan!",
                    "value": [
                        1618.06,
                        1680.84
                    ]
                },
                {
                    "name": "Fantasy Guru Kayden",
                    "value": [
                        1669.0,
                        1703.96
                    ]
                },
                {
                    "name": "Mama Daughter Duo",
                    "value": [
                        1674.46,
                        1721.92
                    ]
                },
                {
                    "name": "Abbey Road to Victory",
                    "value": [
                        1546.74,
                        1644.64
                    ]
                },
                {
                    "name": "Hamlin My Business ",
                    "value": [
                        1906.38,
                        1743.24
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
                    1397.0,
                    1397.0
                ],
                [
                    2080.0,
                    2080.0
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
                        "xAxis": 1749.83,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 1749.83,
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
                    99.98,
                    129.36,
                    137.13,
                    151.67,
                    169.2
                ],
                [
                    108.92,
                    128.5,
                    135.52,
                    142.79,
                    164.23
                ],
                [
                    82.34,
                    120.33,
                    137.53,
                    158.74,
                    178.88
                ],
                [
                    89.6,
                    110.28,
                    126.12,
                    141.24,
                    161.92
                ],
                [
                    77.8,
                    93.64,
                    120.05,
                    137.4,
                    143.7
                ],
                [
                    80.02,
                    115.6,
                    129.14,
                    142.12,
                    171.72
                ],
                [
                    90.74,
                    107.84,
                    119.58,
                    132.22,
                    139.8
                ],
                [
                    73.28,
                    96.94,
                    103.5,
                    125.9,
                    161.64
                ],
                [
                    72.52,
                    106.56,
                    117.44,
                    141.07,
                    159.98
                ],
                [
                    98.46,
                    107.14,
                    116.99,
                    126.72,
                    156.07
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
                    169.2,
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
                    144.36,
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
                    168.3,
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
                    154.4,
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
                    103.98,
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
                    131.44,
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
                    131.46,
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
                    108.02,
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
                    72.52,
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
                    123.4,
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
                    4
                ],
                [
                    0,
                    1,
                    2
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
                    3
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
                    3
                ],
                [
                    3,
                    2,
                    1
                ],
                [
                    0,
                    3,
                    5
                ],
                [
                    1,
                    3,
                    3
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
                    5
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
                    5
                ],
                [
                    2,
                    5,
                    2
                ],
                [
                    3,
                    5,
                    2
                ],
                [
                    0,
                    6,
                    6
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
                    6
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
                    7
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
                    2
                ],
                [
                    2,
                    8,
                    9
                ],
                [
                    3,
                    8,
                    10
                ],
                [
                    0,
                    9,
                    4
                ],
                [
                    1,
                    9,
                    9
                ],
                [
                    2,
                    9,
                    6
                ],
                [
                    3,
                    9,
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
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14
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
            "KTT",
            "RRT",
            "MMT",
            "WKCR",
            "TIB",
            "JST",
            "TOM",
            "HMB",
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
                    10
                ],
                [
                    1,
                    0,
                    2
                ],
                [
                    2,
                    0,
                    6
                ],
                [
                    3,
                    0,
                    10
                ],
                [
                    4,
                    0,
                    1
                ],
                [
                    5,
                    0,
                    8
                ],
                [
                    6,
                    0,
                    7
                ],
                [
                    7,
                    0,
                    2
                ],
                [
                    8,
                    0,
                    6
                ],
                [
                    9,
                    0,
                    4
                ],
                [
                    10,
                    0,
                    10
                ],
                [
                    11,
                    0,
                    10
                ],
                [
                    12,
                    0,
                    10
                ],
                [
                    13,
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
                    7
                ],
                [
                    3,
                    1,
                    3
                ],
                [
                    4,
                    1,
                    6
                ],
                [
                    5,
                    1,
                    6
                ],
                [
                    6,
                    1,
                    8
                ],
                [
                    7,
                    1,
                    9
                ],
                [
                    8,
                    1,
                    5
                ],
                [
                    9,
                    1,
                    5
                ],
                [
                    10,
                    1,
                    8
                ],
                [
                    11,
                    1,
                    9
                ],
                [
                    12,
                    1,
                    6
                ],
                [
                    13,
                    1,
                    10
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
                    0,
                    3,
                    6
                ],
                [
                    1,
                    3,
                    3
                ],
                [
                    2,
                    3,
                    1
                ],
                [
                    3,
                    3,
                    5
                ],
                [
                    4,
                    3,
                    9
                ],
                [
                    5,
                    3,
                    10
                ],
                [
                    6,
                    3,
                    10
                ],
                [
                    7,
                    3,
                    8
                ],
                [
                    8,
                    3,
                    8
                ],
                [
                    9,
                    3,
                    3
                ],
                [
                    10,
                    3,
                    2
                ],
                [
                    11,
                    3,
                    5
                ],
                [
                    12,
                    3,
                    9
                ],
                [
                    13,
                    3,
                    6
                ],
                [
                    0,
                    4,
                    9
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
                    1
                ],
                [
                    6,
                    4,
                    2
                ],
                [
                    7,
                    4,
                    10
                ],
                [
                    8,
                    4,
                    10
                ],
                [
                    9,
                    4,
                    9
                ],
                [
                    10,
                    4,
                    6
                ],
                [
                    11,
                    4,
                    2
                ],
                [
                    12,
                    4,
                    3
                ],
                [
                    13,
                    4,
                    1
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
                    0,
                    7,
                    3
                ],
                [
                    1,
                    7,
                    1
                ],
                [
                    2,
                    7,
                    9
                ],
                [
                    3,
                    7,
                    1
                ],
                [
                    4,
                    7,
                    3
                ],
                [
                    5,
                    7,
                    2
                ],
                [
                    6,
                    7,
                    1
                ],
                [
                    7,
                    7,
                    5
                ],
                [
                    8,
                    7,
                    9
                ],
                [
                    9,
                    7,
                    6
                ],
                [
                    10,
                    7,
                    4
                ],
                [
                    11,
                    7,
                    4
                ],
                [
                    12,
                    7,
                    8
                ],
                [
                    13,
                    7,
                    3
                ],
                [
                    0,
                    8,
                    8
                ],
                [
                    1,
                    8,
                    4
                ],
                [
                    2,
                    8,
                    3
                ],
                [
                    3,
                    8,
                    7
                ],
                [
                    4,
                    8,
                    8
                ],
                [
                    5,
                    8,
                    3
                ],
                [
                    6,
                    8,
                    3
                ],
                [
                    7,
                    8,
                    3
                ],
                [
                    8,
                    8,
                    3
                ],
                [
                    9,
                    8,
                    1
                ],
                [
                    10,
                    8,
                    5
                ],
                [
                    11,
                    8,
                    3
                ],
                [
                    12,
                    8,
                    5
                ],
                [
                    13,
                    8,
                    2
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
            14
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
            "TOM",
            "RRT",
            "TIB",
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
                    0,
                    1,
                    8
                ],
                [
                    1,
                    1,
                    10
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
                    4,
                    1,
                    10
                ],
                [
                    5,
                    1,
                    5
                ],
                [
                    6,
                    1,
                    10
                ],
                [
                    7,
                    1,
                    6
                ],
                [
                    8,
                    1,
                    4
                ],
                [
                    9,
                    1,
                    10
                ],
                [
                    10,
                    1,
                    2
                ],
                [
                    11,
                    1,
                    8
                ],
                [
                    12,
                    1,
                    3
                ],
                [
                    13,
                    1,
                    2
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
                    8
                ],
                [
                    3,
                    2,
                    9
                ],
                [
                    4,
                    2,
                    9
                ],
                [
                    5,
                    2,
                    8
                ],
                [
                    6,
                    2,
                    6
                ],
                [
                    7,
                    2,
                    5
                ],
                [
                    8,
                    2,
                    1
                ],
                [
                    9,
                    2,
                    2
                ],
                [
                    10,
                    2,
                    10
                ],
                [
                    11,
                    2,
                    7
                ],
                [
                    12,
                    2,
                    5
                ],
                [
                    13,
                    2,
                    10
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
                    3
                ],
                [
                    3,
                    3,
                    10
                ],
                [
                    4,
                    3,
                    4
                ],
                [
                    5,
                    3,
                    3
                ],
                [
                    6,
                    3,
                    2
                ],
                [
                    7,
                    3,
                    7
                ],
                [
                    8,
                    3,
                    7
                ],
                [
                    9,
                    3,
                    9
                ],
                [
                    10,
                    3,
                    3
                ],
                [
                    11,
                    3,
                    5
                ],
                [
                    12,
                    3,
                    7
                ],
                [
                    13,
                    3,
                    9
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
            14
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
            "MMT",
            "TOM",
            "WKCR",
            "TIB",
            "HMB",
            "KTT",
            "PONY",
            "RRT",
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
                    5
                ],
                [
                    1,
                    0,
                    9
                ],
                [
                    2,
                    0,
                    5
                ],
                [
                    3,
                    0,
                    10
                ],
                [
                    4,
                    0,
                    8
                ],
                [
                    5,
                    0,
                    9
                ],
                [
                    6,
                    0,
                    4
                ],
                [
                    7,
                    0,
                    1
                ],
                [
                    8,
                    0,
                    1
                ],
                [
                    9,
                    0,
                    9
                ],
                [
                    10,
                    0,
                    9
                ],
                [
                    11,
                    0,
                    9
                ],
                [
                    12,
                    0,
                    4
                ],
                [
                    13,
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
                    5
                ],
                [
                    2,
                    1,
                    1
                ],
                [
                    3,
                    1,
                    6
                ],
                [
                    4,
                    1,
                    9
                ],
                [
                    5,
                    1,
                    6
                ],
                [
                    6,
                    1,
                    7
                ],
                [
                    7,
                    1,
                    9
                ],
                [
                    8,
                    1,
                    6
                ],
                [
                    9,
                    1,
                    5
                ],
                [
                    10,
                    1,
                    5
                ],
                [
                    11,
                    1,
                    6
                ],
                [
                    12,
                    1,
                    6
                ],
                [
                    13,
                    1,
                    9
                ],
                [
                    0,
                    2,
                    4
                ],
                [
                    1,
                    2,
                    1
                ],
                [
                    2,
                    2,
                    7
                ],
                [
                    3,
                    2,
                    8
                ],
                [
                    4,
                    2,
                    10
                ],
                [
                    5,
                    2,
                    10
                ],
                [
                    6,
                    2,
                    5
                ],
                [
                    7,
                    2,
                    4
                ],
                [
                    8,
                    2,
                    10
                ],
                [
                    9,
                    2,
                    7
                ],
                [
                    10,
                    2,
                    6
                ],
                [
                    11,
                    2,
                    7
                ],
                [
                    12,
                    2,
                    8
                ],
                [
                    13,
                    2,
                    2
                ],
                [
                    0,
                    3,
                    7
                ],
                [
                    1,
                    3,
                    9
                ],
                [
                    2,
                    3,
                    3
                ],
                [
                    3,
                    3,
                    7
                ],
                [
                    4,
                    3,
                    5
                ],
                [
                    5,
                    3,
                    1
                ],
                [
                    6,
                    3,
                    6
                ],
                [
                    7,
                    3,
                    6
                ],
                [
                    8,
                    3,
                    7
                ],
                [
                    9,
                    3,
                    10
                ],
                [
                    10,
                    3,
                    2
                ],
                [
                    11,
                    3,
                    8
                ],
                [
                    12,
                    3,
                    9
                ],
                [
                    13,
                    3,
                    6
                ],
                [
                    0,
                    4,
                    6
                ],
                [
                    1,
                    4,
                    6
                ],
                [
                    2,
                    4,
                    9
                ],
                [
                    3,
                    4,
                    3
                ],
                [
                    4,
                    4,
                    3
                ],
                [
                    5,
                    4,
                    4
                ],
                [
                    6,
                    4,
                    8
                ],
                [
                    7,
                    4,
                    8
                ],
                [
                    8,
                    4,
                    4
                ],
                [
                    9,
                    4,
                    3
                ],
                [
                    10,
                    4,
                    3
                ],
                [
                    11,
                    4,
                    10
                ],
                [
                    12,
                    4,
                    10
                ],
                [
                    13,
                    4,
                    5
                ],
                [
                    0,
                    5,
                    2
                ],
                [
                    1,
                    5,
                    2
                ],
                [
                    2,
                    5,
                    10
                ],
                [
                    3,
                    5,
                    1
                ],
                [
                    4,
                    5,
                    1
                ],
                [
                    5,
                    5,
                    3
                ],
                [
                    6,
                    5,
                    9
                ],
                [
                    7,
                    5,
                    10
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
                    8
                ],
                [
                    11,
                    5,
                    5
                ],
                [
                    12,
                    5,
                    5
                ],
                [
                    13,
                    5,
                    10
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
                    0,
                    7,
                    9
                ],
                [
                    1,
                    7,
                    8
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
                    4,
                    7,
                    2
                ],
                [
                    5,
                    7,
                    8
                ],
                [
                    6,
                    7,
                    1
                ],
                [
                    7,
                    7,
                    3
                ],
                [
                    8,
                    7,
                    8
                ],
                [
                    9,
                    7,
                    1
                ],
                [
                    10,
                    7,
                    7
                ],
                [
                    11,
                    7,
                    2
                ],
                [
                    12,
                    7,
                    1
                ],
                [
                    13,
                    7,
                    3
                ],
                [
                    0,
                    8,
                    8
                ],
                [
                    1,
                    8,
                    7
                ],
                [
                    2,
                    8,
                    2
                ],
                [
                    3,
                    8,
                    9
                ],
                [
                    4,
                    8,
                    4
                ],
                [
                    5,
                    8,
                    5
                ],
                [
                    6,
                    8,
                    3
                ],
                [
                    7,
                    8,
                    2
                ],
                [
                    8,
                    8,
                    2
                ],
                [
                    9,
                    8,
                    2
                ],
                [
                    10,
                    8,
                    1
                ],
                [
                    11,
                    8,
                    3
                ],
                [
                    12,
                    8,
                    7
                ],
                [
                    13,
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
            14
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
            "MMT",
            "KTT",
            "TIB",
            "WKCR",
            "RRT",
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
                    0,
                    3,
                    2
                ],
                [
                    1,
                    3,
                    8
                ],
                [
                    2,
                    3,
                    6
                ],
                [
                    3,
                    3,
                    7
                ],
                [
                    4,
                    3,
                    2
                ],
                [
                    5,
                    3,
                    5
                ],
                [
                    6,
                    3,
                    3
                ],
                [
                    7,
                    3,
                    8
                ],
                [
                    8,
                    3,
                    9
                ],
                [
                    9,
                    3,
                    3
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
                    5
                ],
                [
                    0,
                    4,
                    1
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
                    9
                ],
                [
                    4,
                    4,
                    4
                ],
                [
                    5,
                    4,
                    6
                ],
                [
                    6,
                    4,
                    7
                ],
                [
                    7,
                    4,
                    2
                ],
                [
                    8,
                    4,
                    10
                ],
                [
                    9,
                    4,
                    4
                ],
                [
                    10,
                    4,
                    6
                ],
                [
                    11,
                    4,
                    2
                ],
                [
                    12,
                    4,
                    7
                ],
                [
                    13,
                    4,
                    8
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
                    3
                ],
                [
                    3,
                    5,
                    6
                ],
                [
                    4,
                    5,
                    9
                ],
                [
                    5,
                    5,
                    1
                ],
                [
                    6,
                    5,
                    4
                ],
                [
                    7,
                    5,
                    1
                ],
                [
                    8,
                    5,
                    1
                ],
                [
                    9,
                    5,
                    7
                ],
                [
                    10,
                    5,
                    9
                ],
                [
                    11,
                    5,
                    3
                ],
                [
                    12,
                    5,
                    8
                ],
                [
                    13,
                    5,
                    9
                ],
                [
                    0,
                    6,
                    8
                ],
                [
                    1,
                    6,
                    3
                ],
                [
                    2,
                    6,
                    10
                ],
                [
                    3,
                    6,
                    10
                ],
                [
                    4,
                    6,
                    10
                ],
                [
                    5,
                    6,
                    3
                ],
                [
                    6,
                    6,
                    2
                ],
                [
                    7,
                    6,
                    7
                ],
                [
                    8,
                    6,
                    3
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
                    6
                ],
                [
                    12,
                    6,
                    1
                ],
                [
                    13,
                    6,
                    7
                ],
                [
                    0,
                    7,
                    5
                ],
                [
                    1,
                    7,
                    2
                ],
                [
                    2,
                    7,
                    1
                ],
                [
                    3,
                    7,
                    4
                ],
                [
                    4,
                    7,
                    7
                ],
                [
                    5,
                    7,
                    4
                ],
                [
                    6,
                    7,
                    8
                ],
                [
                    7,
                    7,
                    4
                ],
                [
                    8,
                    7,
                    4
                ],
                [
                    9,
                    7,
                    6
                ],
                [
                    10,
                    7,
                    4
                ],
                [
                    11,
                    7,
                    7
                ],
                [
                    12,
                    7,
                    5
                ],
                [
                    13,
                    7,
                    9
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
            "Week 14"
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
                93.5
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
                96.8
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
                90.8
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
                99.7
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
                96.4
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
                67.3
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
                75.5
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
                88.8
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
                72.5
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
                93.7
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
                        1.6,
                        0.2,
                        -2.5
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
                        -0.7,
                        1.4,
                        3.3
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
                        0.4,
                        0.3,
                        -0.3
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
                        0.8,
                        0.6,
                        -1.2,
                        -2.0
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
                        -0.6,
                        0.7
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
                        -1.2,
                        -0.3,
                        1.1,
                        2.6
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
                        -1.0,
                        0.0,
                        0.4
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
                        -1.2,
                        -1.7,
                        -0.1,
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
                        1.7,
                        -0.2,
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
                        -1.0,
                        -0.5
                    ],
                    "name": "Fantasy Guru Kayden"
                }
            ]
        }
    ]
}
```

