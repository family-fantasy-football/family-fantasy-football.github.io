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


The current top scorer is: Christian Ratcliff (0.00)

The current bottom scorer is: Christian Ratcliff (0.00)




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
            "name": "30 Years of Tears",
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
                "formatter": "30 Years of ..."
            }
        },
        {
            "name": "90s MonCon",
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
                "formatter": "90s MonCon"
            }
        },
        {
            "name": "Abbey's TNT Team ",
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
                "formatter": "Abbey's TNT ..."
            }
        },
        {
            "name": "Americas Team ",
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
                "formatter": "Fantasy Guru..."
            }
        },
        {
            "name": "Hamlin My Business ",
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
                "formatter": "Hamlin My Bu..."
            }
        },
        {
            "name": "Mama Daughter Duo",
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
            "name": "TBD",
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
                "formatter": "TBD"
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
        "min": -150.0,
        "max": 150.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": -150.0,
        "max": 150.0
    },
    "series": [
        {
            "name": "Teams",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                {
                    "name": "TBD",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "90s MonCon",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "30 Years of Tears",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "Americas Team ",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "Michael's Managable Team",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "To Infinity and Bijan!",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "Fantasy Guru Kayden",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "Mama Daughter Duo",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "Abbey's TNT Team ",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "Hamlin My Business ",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "Emma's Excellent Team",
                    "value": [
                        0.0,
                        0.0
                    ]
                },
                {
                    "name": "Big Titi Energy",
                    "value": [
                        0.0,
                        0.0
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
                    -150.0,
                    -150.0
                ],
                [
                    150.0,
                    150.0
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
                        "xAxis": 0.0,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 0.0,
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
            "CTR",
            "90s",
            "TOM",
            "RRT",
            "MMT",
            "TIB",
            "KTT",
            "JST",
            "ARV",
            "HMB",
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
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    0,
                    0.0,
                    "CTR"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    1,
                    0.0,
                    "90s"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    2,
                    0.0,
                    "TOM"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
                ],
                [
                    3,
                    0.0,
                    "RRT"
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
                    4,
                    0.0,
                    "MMT"
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
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    6,
                    0.0,
                    "KTT"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    7,
                    0.0,
                    "JST"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    8,
                    0.0,
                    "ARV"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
                ],
                [
                    9,
                    0.0,
                    "HMB"
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
            "CTR",
            "90s",
            "TOM",
            "RRT",
            "MMT",
            "TIB",
            "KTT",
            "JST",
            "ARV",
            "HMB",
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
                    6
                ],
                [
                    1,
                    0,
                    6
                ],
                [
                    2,
                    0,
                    6
                ],
                [
                    3,
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
                    6
                ],
                [
                    0,
                    2,
                    6
                ],
                [
                    1,
                    2,
                    6
                ],
                [
                    2,
                    2,
                    6
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
                    6
                ],
                [
                    3,
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
                    6
                ],
                [
                    2,
                    5,
                    6
                ],
                [
                    3,
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
                    6
                ],
                [
                    2,
                    6,
                    6
                ],
                [
                    3,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    6
                ],
                [
                    1,
                    7,
                    6
                ],
                [
                    2,
                    7,
                    6
                ],
                [
                    3,
                    7,
                    6
                ],
                [
                    0,
                    8,
                    6
                ],
                [
                    1,
                    8,
                    6
                ],
                [
                    2,
                    8,
                    6
                ],
                [
                    3,
                    8,
                    6
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
                    6
                ],
                [
                    3,
                    9,
                    6
                ],
                [
                    0,
                    10,
                    6
                ],
                [
                    1,
                    10,
                    6
                ],
                [
                    2,
                    10,
                    6
                ],
                [
                    3,
                    10,
                    6
                ],
                [
                    0,
                    11,
                    6
                ],
                [
                    1,
                    11,
                    6
                ],
                [
                    2,
                    11,
                    6
                ],
                [
                    3,
                    11,
                    6
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
            "ARV",
            "BTE",
            "CTR",
            "EET",
            "HMB",
            "JST",
            "KTT",
            "MMT",
            "RRT",
            "TIB",
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
                    6
                ],
                [
                    0,
                    1,
                    6
                ],
                [
                    0,
                    2,
                    6
                ],
                [
                    0,
                    3,
                    6
                ],
                [
                    0,
                    4,
                    6
                ],
                [
                    0,
                    5,
                    6
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    6
                ],
                [
                    0,
                    8,
                    6
                ],
                [
                    0,
                    9,
                    6
                ],
                [
                    0,
                    10,
                    6
                ],
                [
                    0,
                    11,
                    6
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
            "90s",
            "ARV",
            "BTE",
            "CTR",
            "EET",
            "HMB",
            "JST",
            "KTT",
            "MMT",
            "RRT",
            "TIB",
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
                    6
                ],
                [
                    0,
                    1,
                    6
                ],
                [
                    0,
                    2,
                    6
                ],
                [
                    0,
                    3,
                    6
                ],
                [
                    0,
                    4,
                    6
                ],
                [
                    0,
                    5,
                    6
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    6
                ],
                [
                    0,
                    8,
                    6
                ],
                [
                    0,
                    9,
                    6
                ],
                [
                    0,
                    10,
                    6
                ],
                [
                    0,
                    11,
                    6
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
            "90s",
            "ARV",
            "BTE",
            "CTR",
            "EET",
            "HMB",
            "JST",
            "KTT",
            "MMT",
            "RRT",
            "TIB",
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
                    6
                ],
                [
                    0,
                    1,
                    6
                ],
                [
                    0,
                    2,
                    6
                ],
                [
                    0,
                    3,
                    6
                ],
                [
                    0,
                    4,
                    6
                ],
                [
                    0,
                    5,
                    6
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    6
                ],
                [
                    0,
                    8,
                    6
                ],
                [
                    0,
                    9,
                    6
                ],
                [
                    0,
                    10,
                    6
                ],
                [
                    0,
                    11,
                    6
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
            "90s",
            "ARV",
            "BTE",
            "CTR",
            "EET",
            "HMB",
            "JST",
            "KTT",
            "MMT",
            "RRT",
            "TIB",
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
                    6
                ],
                [
                    0,
                    1,
                    6
                ],
                [
                    0,
                    2,
                    6
                ],
                [
                    0,
                    3,
                    6
                ],
                [
                    0,
                    4,
                    6
                ],
                [
                    0,
                    5,
                    6
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    0,
                    7,
                    6
                ],
                [
                    0,
                    8,
                    6
                ],
                [
                    0,
                    9,
                    6
                ],
                [
                    0,
                    10,
                    6
                ],
                [
                    0,
                    11,
                    6
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
            "CTR",
            "90s",
            "TOM",
            "RRT",
            "MMT",
            "TIB",
            "KTT",
            "JST",
            "ARV",
            "HMB",
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
            "Week 1"
        ]
    },
    "yAxis": {
        "type": "value",
        "name": "Efficiency %"
    },
    "series": [
        {
            "name": "CTR",
            "type": "line",
            "data": []
        },
        {
            "name": "90s",
            "type": "line",
            "data": []
        },
        {
            "name": "TOM",
            "type": "line",
            "data": []
        },
        {
            "name": "RRT",
            "type": "line",
            "data": []
        },
        {
            "name": "MMT",
            "type": "line",
            "data": []
        },
        {
            "name": "TIB",
            "type": "line",
            "data": []
        },
        {
            "name": "KTT",
            "type": "line",
            "data": []
        },
        {
            "name": "JST",
            "type": "line",
            "data": []
        },
        {
            "name": "ARV",
            "type": "line",
            "data": []
        },
        {
            "name": "HMB",
            "type": "line",
            "data": []
        },
        {
            "name": "EET",
            "type": "line",
            "data": []
        },
        {
            "name": "BTE",
            "type": "line",
            "data": []
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
            "name": "TBD",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "TBD"
                }
            ]
        },
        {
            "name": "90s MonCon",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "90s MonCon"
                }
            ]
        },
        {
            "name": "30 Years of Tears",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "30 Years of Tears"
                }
            ]
        },
        {
            "name": "Americas Team ",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "Americas Team "
                }
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "Michael's Managable Team"
                }
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "To Infinity and Bijan!"
                }
            ]
        },
        {
            "name": "Fantasy Guru Kayden",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "Fantasy Guru Kayden"
                }
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
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
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "Abbey's TNT Team "
                }
            ]
        },
        {
            "name": "Hamlin My Business ",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "Hamlin My Business "
                }
            ]
        },
        {
            "name": "Emma's Excellent Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.0,
                        0.0,
                        0.0,
                        0.0
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
                        0.0,
                        0.0,
                        0.0,
                        0.0
                    ],
                    "name": "Big Titi Energy"
                }
            ]
        }
    ]
}
```

