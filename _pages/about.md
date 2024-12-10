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

## Welcome to the site for the Family Fantasy Footbal League! We are currently in the 2024-25 season. This site is clearly still under development

<div style="margin-bottom: 30px;">

</div>


The current top scorer is: Kyle Hamlin (1762.02)

The current top scorer is: Abbey Hamlin and Christine Hamlin (1438.72)

Highest Scoring Week: Kyle Hamlin - 180.62 points (Week 6)

Lowest Scoring Week: Abbey Hamlin and Christine Hamlin - 73.28 points (Week 7)

Luckiest Team: Tom Ratcliff (1.4) Wins Above Expected

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
            13
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
                2
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
                3
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



### Average Position Rankings
```echarts
{
    "grid": {
        "top": "10%",
        "bottom": "15%",
        "left": "5%",
        "right": "0%"
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
                    2
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
                    3
                ],
                [
                    1,
                    1,
                    5
                ],
                [
                    2,
                    1,
                    2
                ],
                [
                    3,
                    1,
                    3
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
                    4
                ],
                [
                    1,
                    3,
                    3
                ],
                [
                    2,
                    3,
                    9
                ],
                [
                    3,
                    3,
                    7
                ],
                [
                    0,
                    4,
                    9
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
                    6
                ],
                [
                    0,
                    5,
                    7
                ],
                [
                    1,
                    5,
                    4
                ],
                [
                    2,
                    5,
                    1
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
                    9
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
                    0,
                    7,
                    8
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
                    8
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
        "right": "0%"
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
            13
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
            "WKCR",
            "RRT",
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
                    0,
                    2,
                    9
                ],
                [
                    1,
                    2,
                    9
                ],
                [
                    2,
                    2,
                    10
                ],
                [
                    3,
                    2,
                    8
                ],
                [
                    4,
                    2,
                    2
                ],
                [
                    5,
                    2,
                    1
                ],
                [
                    6,
                    2,
                    2
                ],
                [
                    7,
                    2,
                    10
                ],
                [
                    8,
                    2,
                    10
                ],
                [
                    9,
                    2,
                    9
                ],
                [
                    10,
                    2,
                    6
                ],
                [
                    11,
                    2,
                    2
                ],
                [
                    12,
                    2,
                    3
                ],
                [
                    0,
                    3,
                    4
                ],
                [
                    1,
                    3,
                    8
                ],
                [
                    2,
                    3,
                    4
                ],
                [
                    3,
                    3,
                    4
                ],
                [
                    4,
                    3,
                    10
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
                    7
                ],
                [
                    8,
                    3,
                    4
                ],
                [
                    9,
                    3,
                    8
                ],
                [
                    10,
                    3,
                    3
                ],
                [
                    11,
                    3,
                    8
                ],
                [
                    12,
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
        "right": "0%"
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
            13
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
            "TIB",
            "RRT",
            "HMB",
            "ARV",
            "MMT",
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
                    0,
                    2,
                    9
                ],
                [
                    1,
                    2,
                    6
                ],
                [
                    2,
                    2,
                    3
                ],
                [
                    3,
                    2,
                    10
                ],
                [
                    4,
                    2,
                    4
                ],
                [
                    5,
                    2,
                    3
                ],
                [
                    6,
                    2,
                    2
                ],
                [
                    7,
                    2,
                    7
                ],
                [
                    8,
                    2,
                    7
                ],
                [
                    9,
                    2,
                    9
                ],
                [
                    10,
                    2,
                    3
                ],
                [
                    11,
                    2,
                    5
                ],
                [
                    12,
                    2,
                    7
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
                    1
                ],
                [
                    3,
                    4,
                    7
                ],
                [
                    4,
                    4,
                    8
                ],
                [
                    5,
                    4,
                    2
                ],
                [
                    6,
                    4,
                    9
                ],
                [
                    7,
                    4,
                    1
                ],
                [
                    8,
                    4,
                    5
                ],
                [
                    9,
                    4,
                    5
                ],
                [
                    10,
                    4,
                    8
                ],
                [
                    11,
                    4,
                    2
                ],
                [
                    12,
                    4,
                    6
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
                    0,
                    6,
                    2
                ],
                [
                    1,
                    6,
                    3
                ],
                [
                    2,
                    6,
                    9
                ],
                [
                    3,
                    6,
                    8
                ],
                [
                    4,
                    6,
                    2
                ],
                [
                    5,
                    6,
                    7
                ],
                [
                    6,
                    6,
                    5
                ],
                [
                    7,
                    6,
                    2
                ],
                [
                    8,
                    6,
                    2
                ],
                [
                    9,
                    6,
                    8
                ],
                [
                    10,
                    6,
                    1
                ],
                [
                    11,
                    6,
                    9
                ],
                [
                    12,
                    6,
                    10
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
        "right": "0%"
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
            13
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
            "ARV",
            "MMT",
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
                    7
                ],
                [
                    3,
                    0,
                    8
                ],
                [
                    4,
                    0,
                    10
                ],
                [
                    5,
                    0,
                    10
                ],
                [
                    6,
                    0,
                    5
                ],
                [
                    7,
                    0,
                    4
                ],
                [
                    8,
                    0,
                    10
                ],
                [
                    9,
                    0,
                    7
                ],
                [
                    10,
                    0,
                    6
                ],
                [
                    11,
                    0,
                    7
                ],
                [
                    12,
                    0,
                    8
                ],
                [
                    0,
                    1,
                    5
                ],
                [
                    1,
                    1,
                    9
                ],
                [
                    2,
                    1,
                    5
                ],
                [
                    3,
                    1,
                    10
                ],
                [
                    4,
                    1,
                    8
                ],
                [
                    5,
                    1,
                    9
                ],
                [
                    6,
                    1,
                    4
                ],
                [
                    7,
                    1,
                    1
                ],
                [
                    8,
                    1,
                    1
                ],
                [
                    9,
                    1,
                    9
                ],
                [
                    10,
                    1,
                    9
                ],
                [
                    11,
                    1,
                    9
                ],
                [
                    12,
                    1,
                    4
                ],
                [
                    0,
                    2,
                    10
                ],
                [
                    1,
                    2,
                    5
                ],
                [
                    2,
                    2,
                    1
                ],
                [
                    3,
                    2,
                    6
                ],
                [
                    4,
                    2,
                    9
                ],
                [
                    5,
                    2,
                    6
                ],
                [
                    6,
                    2,
                    7
                ],
                [
                    7,
                    2,
                    9
                ],
                [
                    8,
                    2,
                    6
                ],
                [
                    9,
                    2,
                    5
                ],
                [
                    10,
                    2,
                    5
                ],
                [
                    11,
                    2,
                    6
                ],
                [
                    12,
                    2,
                    6
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
        "right": "0%"
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
            13
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
            "MMT",
            "ARV",
            "KTT",
            "TIB",
            "WKCR",
            "HMB",
            "JST",
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
                    0,
                    2,
                    2
                ],
                [
                    1,
                    2,
                    8
                ],
                [
                    2,
                    2,
                    6
                ],
                [
                    3,
                    2,
                    7
                ],
                [
                    4,
                    2,
                    2
                ],
                [
                    5,
                    2,
                    5
                ],
                [
                    6,
                    2,
                    3
                ],
                [
                    7,
                    2,
                    8
                ],
                [
                    8,
                    2,
                    9
                ],
                [
                    9,
                    2,
                    3
                ],
                [
                    10,
                    2,
                    9
                ],
                [
                    11,
                    2,
                    9
                ],
                [
                    12,
                    2,
                    4
                ],
                [
                    0,
                    3,
                    6
                ],
                [
                    1,
                    3,
                    10
                ],
                [
                    2,
                    3,
                    8
                ],
                [
                    3,
                    3,
                    3
                ],
                [
                    4,
                    3,
                    5
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
                    3
                ],
                [
                    8,
                    3,
                    2
                ],
                [
                    9,
                    3,
                    1
                ],
                [
                    10,
                    3,
                    7
                ],
                [
                    11,
                    3,
                    4
                ],
                [
                    12,
                    3,
                    6
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
                    0,
                    7,
                    4
                ],
                [
                    1,
                    7,
                    1
                ],
                [
                    2,
                    7,
                    5
                ],
                [
                    3,
                    7,
                    2
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
                    5
                ],
                [
                    7,
                    7,
                    9
                ],
                [
                    8,
                    7,
                    6
                ],
                [
                    9,
                    7,
                    9
                ],
                [
                    10,
                    7,
                    3
                ],
                [
                    11,
                    7,
                    5
                ],
                [
                    12,
                    7,
                    10
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
                    2,
                    9,
                    1
                ],
                [
                    3,
                    9,
                    4
                ],
                [
                    4,
                    9,
                    7
                ],
                [
                    5,
                    9,
                    4
                ],
                [
                    6,
                    9,
                    8
                ],
                [
                    7,
                    9,
                    4
                ],
                [
                    8,
                    9,
                    4
                ],
                [
                    9,
                    9,
                    6
                ],
                [
                    10,
                    9,
                    4
                ],
                [
                    11,
                    9,
                    7
                ],
                [
                    12,
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
