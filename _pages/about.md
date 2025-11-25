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
<style>
  table[data-toggle="table"] tbody td {
    color: #2c3e50 !important;
  }
</style>

<div style="text-align: center; padding: 40px 0 30px 0;">
  <p style="font-size: 20px; color: #555; font-weight: 500;">2025-26 Season</p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">
  <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">🏆 Top Scorer</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Michael Ratcliff</div>
    <div style="font-size: 18px; opacity: 0.95;">1604.73 points</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">📉 Bottom Scorer</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Emma Grau</div>
    <div style="font-size: 18px; opacity: 0.95;">1048.88 points</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">🔥 Highest Week</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Michael Ratcliff</div>
    <div style="font-size: 18px; opacity: 0.95;">187.93 pts (Week 7)</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">❄️ Lowest Week</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Ryan Ratcliff</div>
    <div style="font-size: 18px; opacity: 0.95;">60.54 pts (Week 8)</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: #2c3e50;">
    <div style="font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">🍀 Luckiest</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Kyle Hamlin</div>
    <div style="font-size: 18px;">+1.7 wins vs expected</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: #2c3e50;">
    <div style="font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">😢 Unluckiest</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Connor Dickson and Monika Monko</div>
    <div style="font-size: 18px;">-3.3 wins vs expected</div>
  </div>
</div>

<div style="background: white; padding: 35px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin: 40px 0;">
  <h2 style="font-size: 32px; font-weight: 700; color: #2c3e50; margin: 0 0 25px 0; padding-bottom: 15px; border-bottom: 3px solid #667eea;">
    📊 League Standings
  </h2>
<table
    data-click-to-select="true"
    data-pagination="false"
    data-search="false"
    data-toggle="table"
    data-url="{{ "/assets/json/standings.json"}}">
    <thead style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
        <tr>
            <th data-field="team" 
                data-halign="left" 
                data-align="left" 
                data-sortable="true"
                style="color: white; font-weight: 600; padding: 15px;">Team</th>
            <th data-field="record" 
                data-halign="center" 
                data-align="center" 
                data-sortable="true"
                data-sort-name="record_sort"
                style="color: white; font-weight: 600; padding: 15px;">Record</th>
            <th data-field="record_sort" data-sortable="true" data-visible="false">Record Sort</th>
            <th data-field="points_for" 
                data-halign="center" 
                data-align="center" 
                data-sortable="true"
                data-sort-name="points_for_sort"
                style="color: white; font-weight: 600; padding: 15px;">Points For</th>
            <th data-field="points_for_sort" data-sortable="true" data-visible="false">PF Sort</th>
            <th data-field="points_against" 
                data-halign="center" 
                data-align="center" 
                data-sortable="true"
                data-sort-name="points_against_sort"
                style="color: white; font-weight: 600; padding: 15px;">Points Against</th>
            <th data-field="points_against_sort" data-sortable="true" data-visible="false">PA Sort</th>
                        <th data-field="power_rank" 
                data-halign="center" 
                data-align="center" 
                data-sortable="true"
                style="color: white; font-weight: 600; padding: 15px;">All-Play Rank</th>
            <th data-field="last3" 
                data-halign="center" 
                data-align="center" 
                data-sortable="true"
                style="color: white; font-weight: 600; padding: 15px;">Last 3</th>
        </tr>
    </thead>
</table>
</div>
---

## 📈 Standings Movement
```echarts
{
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
            12
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
                "color": "#f7b6d2"
            },
            "itemStyle": {
                "color": "#f7b6d2"
            },
            "data": [
                7,
                4,
                3,
                1,
                3,
                7,
                8,
                9,
                9,
                9,
                9,
                9
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
            "name": "Abbey's TNT Team",
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
                5,
                4,
                3,
                4,
                4,
                7,
                6,
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
            "name": "Americas Team",
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
                12,
                10,
                10,
                10,
                8,
                6,
                4,
                6,
                6,
                3,
                3,
                2
            ],
            "symbol": "circle",
            "symbolSize": 12,
            "label": {
                "show": false,
                "position": "right",
                "formatter": "Americas Team"
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
                11,
                12,
                11,
                11,
                11,
                11,
                11,
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
                12,
                11,
                12,
                12,
                12,
                12,
                12,
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
                "color": "#98df8a"
            },
            "itemStyle": {
                "color": "#98df8a"
            },
            "data": [
                1,
                1,
                1,
                2,
                1,
                3,
                5,
                3,
                3,
                5,
                4,
                4
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
                6,
                9,
                9,
                7,
                5,
                5,
                4,
                7,
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
                "color": "#c49c94"
            },
            "itemStyle": {
                "color": "#c49c94"
            },
            "data": [
                10,
                9,
                7,
                9,
                7,
                5,
                6,
                8,
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
                "formatter": "Mcconky Donk..."
            }
        },
        {
            "name": "Michael's Managable Team",
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
                5,
                2,
                2,
                3,
                4,
                2,
                2,
                2,
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
                7,
                6,
                8,
                9,
                7,
                7,
                6,
                5,
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
                3,
                6,
                5,
                2,
                1,
                1,
                1,
                2,
                2,
                1,
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
                10,
                10,
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

---

## 🎯 Points For vs Points Against
```echarts
{
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
            "Americas Team",
            "Michael's Managable Team",
            "To Infinity and Bijan!",
            "Mcconky Donkeys",
            "Mama Daughter Duo",
            "Abbey's TNT Team",
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
        "min": 899.0,
        "max": 1755.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": 899.0,
        "max": 1755.0
    },
    "series": [
        {
            "name": "Third Time's the Charm?",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1514.23,
                    1357.96
                ]
            ]
        },
        {
            "name": "90s MonCon",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1476.95,
                    1484.89
                ]
            ]
        },
        {
            "name": "Rookie Mistake",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1415.98,
                    1341.54
                ]
            ]
        },
        {
            "name": "Americas Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1577.86,
                    1401.79
                ]
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1604.73,
                    1328.29
                ]
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1241.81,
                    1394.3
                ]
            ]
        },
        {
            "name": "Mcconky Donkeys",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1245.5,
                    1268.17
                ]
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1524.42,
                    1453.21
                ]
            ]
        },
        {
            "name": "Abbey's TNT Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1361.92,
                    1294.37
                ]
            ]
        },
        {
            "name": "Game of Zones - House Hamlin",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1454.76,
                    1287.59
                ]
            ]
        },
        {
            "name": "Emma's Excellent Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1048.88,
                    1440.23
                ]
            ]
        },
        {
            "name": "Big Titi Energy",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    1149.81,
                    1564.51
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
                    899.0,
                    899.0
                ],
                [
                    1755.0,
                    1755.0
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
                        "xAxis": 1384.74,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 1384.74,
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

---

## 📦 Weekly Score Distribution
```echarts
{
    "xAxis": {
        "type": "category",
        "name": "Teams",
        "nameLocation": "middle",
        "nameGap": 30,
        "data": [
            "MMT",
            "RRT",
            "TTC",
            "HMB",
            "ARV",
            "JST",
            "TOM",
            "KTT",
            "90s",
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
                    90.38,
                    118.23,
                    134.52,
                    142.94,
                    180.0
                ],
                [
                    60.54,
                    109.44,
                    134.68,
                    158.05,
                    178.27
                ],
                [
                    85.3,
                    104.36,
                    116.81,
                    155.7,
                    165.67
                ],
                [
                    91.16,
                    109.48,
                    121.04,
                    128.94,
                    158.14
                ],
                [
                    67.33,
                    98.62,
                    111.56,
                    126.56,
                    157.57
                ],
                [
                    104.14,
                    122.86,
                    128.25,
                    135.34,
                    154.05
                ],
                [
                    94.53,
                    103.49,
                    120.3,
                    125.41,
                    156.21
                ],
                [
                    77.92,
                    87.32,
                    93.96,
                    123.27,
                    153.43
                ],
                [
                    67.71,
                    96.94,
                    127.5,
                    149.54,
                    170.76
                ],
                [
                    65.2,
                    91.2,
                    103.37,
                    116.63,
                    137.55
                ],
                [
                    64.16,
                    77.8,
                    82.06,
                    104.59,
                    144.77
                ],
                [
                    60.7,
                    72.21,
                    85.54,
                    106.1,
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
                    111.95,
                    "MMT"
                ],
                [
                    0,
                    141.03,
                    "MMT"
                ],
                [
                    0,
                    148.67,
                    "MMT"
                ],
                [
                    0,
                    136.89,
                    "MMT"
                ],
                [
                    0,
                    119.91,
                    "MMT"
                ],
                [
                    0,
                    132.15,
                    "MMT"
                ],
                [
                    0,
                    187.93,
                    "MMT"
                ],
                [
                    0,
                    139.86,
                    "MMT"
                ],
                [
                    0,
                    120.01,
                    "MMT"
                ],
                [
                    0,
                    113.2,
                    "MMT"
                ],
                [
                    0,
                    90.38,
                    "MMT"
                ],
                [
                    0,
                    162.75,
                    "MMT"
                ],
                [
                    1,
                    80.1,
                    "RRT"
                ],
                [
                    1,
                    148.62,
                    "RRT"
                ],
                [
                    1,
                    144.61,
                    "RRT"
                ],
                [
                    1,
                    111.53,
                    "RRT"
                ],
                [
                    1,
                    178.27,
                    "RRT"
                ],
                [
                    1,
                    124.74,
                    "RRT"
                ],
                [
                    1,
                    173.1,
                    "RRT"
                ],
                [
                    1,
                    60.54,
                    "RRT"
                ],
                [
                    1,
                    175.89,
                    "RRT"
                ],
                [
                    1,
                    124.27,
                    "RRT"
                ],
                [
                    1,
                    103.16,
                    "RRT"
                ],
                [
                    1,
                    153.03,
                    "RRT"
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
                    85.3,
                    "TTC"
                ],
                [
                    2,
                    156.86,
                    "TTC"
                ],
                [
                    2,
                    165.45,
                    "TTC"
                ],
                [
                    2,
                    165.67,
                    "TTC"
                ],
                [
                    2,
                    141.2,
                    "TTC"
                ],
                [
                    2,
                    116.43,
                    "TTC"
                ],
                [
                    2,
                    99.0,
                    "TTC"
                ],
                [
                    2,
                    93.81,
                    "TTC"
                ],
                [
                    2,
                    155.31,
                    "TTC"
                ],
                [
                    2,
                    117.19,
                    "TTC"
                ],
                [
                    3,
                    176.38,
                    "HMB"
                ],
                [
                    3,
                    119.75,
                    "HMB"
                ],
                [
                    3,
                    114.94,
                    "HMB"
                ],
                [
                    3,
                    135.24,
                    "HMB"
                ],
                [
                    3,
                    122.87,
                    "HMB"
                ],
                [
                    3,
                    101.21,
                    "HMB"
                ],
                [
                    3,
                    91.16,
                    "HMB"
                ],
                [
                    3,
                    138.97,
                    "HMB"
                ],
                [
                    3,
                    126.84,
                    "HMB"
                ],
                [
                    3,
                    92.83,
                    "HMB"
                ],
                [
                    3,
                    122.34,
                    "HMB"
                ],
                [
                    3,
                    112.23,
                    "HMB"
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
                    4,
                    97.27,
                    "ARV"
                ],
                [
                    4,
                    101.89,
                    "ARV"
                ],
                [
                    4,
                    67.33,
                    "ARV"
                ],
                [
                    4,
                    150.48,
                    "ARV"
                ],
                [
                    4,
                    99.07,
                    "ARV"
                ],
                [
                    4,
                    110.02,
                    "ARV"
                ],
                [
                    4,
                    83.6,
                    "ARV"
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
                    120.25,
                    "JST"
                ],
                [
                    5,
                    152.0,
                    "JST"
                ],
                [
                    5,
                    141.57,
                    "JST"
                ],
                [
                    5,
                    133.26,
                    "JST"
                ],
                [
                    5,
                    133.04,
                    "JST"
                ],
                [
                    5,
                    102.87,
                    "JST"
                ],
                [
                    5,
                    77.82,
                    "JST"
                ],
                [
                    5,
                    130.12,
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
                    120.4,
                    "TOM"
                ],
                [
                    6,
                    115.52,
                    "TOM"
                ],
                [
                    6,
                    102.96,
                    "TOM"
                ],
                [
                    6,
                    122.09,
                    "TOM"
                ],
                [
                    6,
                    126.05,
                    "TOM"
                ],
                [
                    6,
                    126.88,
                    "TOM"
                ],
                [
                    6,
                    102.28,
                    "TOM"
                ],
                [
                    6,
                    120.19,
                    "TOM"
                ],
                [
                    7,
                    101.15,
                    "KTT"
                ],
                [
                    7,
                    99.4,
                    "KTT"
                ],
                [
                    7,
                    88.53,
                    "KTT"
                ],
                [
                    7,
                    86.76,
                    "KTT"
                ],
                [
                    7,
                    129.8,
                    "KTT"
                ],
                [
                    7,
                    153.43,
                    "KTT"
                ],
                [
                    7,
                    87.51,
                    "KTT"
                ],
                [
                    7,
                    122.34,
                    "KTT"
                ],
                [
                    7,
                    88.34,
                    "KTT"
                ],
                [
                    7,
                    126.06,
                    "KTT"
                ],
                [
                    7,
                    84.26,
                    "KTT"
                ],
                [
                    7,
                    77.92,
                    "KTT"
                ],
                [
                    8,
                    111.47,
                    "90s"
                ],
                [
                    8,
                    157.15,
                    "90s"
                ],
                [
                    8,
                    170.76,
                    "90s"
                ],
                [
                    8,
                    115.91,
                    "90s"
                ],
                [
                    8,
                    159.49,
                    "90s"
                ],
                [
                    8,
                    67.71,
                    "90s"
                ],
                [
                    8,
                    97.89,
                    "90s"
                ],
                [
                    8,
                    144.17,
                    "90s"
                ],
                [
                    8,
                    139.1,
                    "90s"
                ],
                [
                    8,
                    147.01,
                    "90s"
                ],
                [
                    8,
                    72.21,
                    "90s"
                ],
                [
                    8,
                    94.08,
                    "90s"
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
                    9,
                    65.2,
                    "TIB"
                ],
                [
                    9,
                    95.41,
                    "TIB"
                ],
                [
                    9,
                    95.77,
                    "TIB"
                ],
                [
                    9,
                    111.2,
                    "TIB"
                ],
                [
                    9,
                    100.34,
                    "TIB"
                ],
                [
                    9,
                    106.4,
                    "TIB"
                ],
                [
                    9,
                    73.62,
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
                    10,
                    87.79,
                    "BTE"
                ],
                [
                    10,
                    95.89,
                    "BTE"
                ],
                [
                    10,
                    154.0,
                    "BTE"
                ],
                [
                    10,
                    130.69,
                    "BTE"
                ],
                [
                    10,
                    78.12,
                    "BTE"
                ],
                [
                    10,
                    64.16,
                    "BTE"
                ],
                [
                    10,
                    76.84,
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
                ],
                [
                    11,
                    89.62,
                    "EET"
                ],
                [
                    11,
                    66.19,
                    "EET"
                ],
                [
                    11,
                    60.7,
                    "EET"
                ],
                [
                    11,
                    107.3,
                    "EET"
                ],
                [
                    11,
                    76.42,
                    "EET"
                ],
                [
                    11,
                    106.22,
                    "EET"
                ],
                [
                    11,
                    81.46,
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

---

## 🏈 Average Position Rankings
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
            "MMT",
            "RRT",
            "TTC",
            "HMB",
            "ARV",
            "JST",
            "TOM",
            "KTT",
            "90s",
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
                    2
                ],
                [
                    1,
                    0,
                    5
                ],
                [
                    2,
                    0,
                    7
                ],
                [
                    3,
                    0,
                    2
                ],
                [
                    0,
                    1,
                    4
                ],
                [
                    1,
                    1,
                    9
                ],
                [
                    2,
                    1,
                    1
                ],
                [
                    3,
                    1,
                    1
                ],
                [
                    0,
                    2,
                    1
                ],
                [
                    1,
                    2,
                    3
                ],
                [
                    2,
                    2,
                    10
                ],
                [
                    3,
                    2,
                    10
                ],
                [
                    0,
                    3,
                    3
                ],
                [
                    1,
                    3,
                    10
                ],
                [
                    2,
                    3,
                    3
                ],
                [
                    3,
                    3,
                    4
                ],
                [
                    0,
                    4,
                    9
                ],
                [
                    1,
                    4,
                    7
                ],
                [
                    2,
                    4,
                    8
                ],
                [
                    3,
                    4,
                    3
                ],
                [
                    0,
                    5,
                    5
                ],
                [
                    1,
                    5,
                    2
                ],
                [
                    2,
                    5,
                    6
                ],
                [
                    3,
                    5,
                    5
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
                    4
                ],
                [
                    3,
                    6,
                    12
                ],
                [
                    0,
                    7,
                    7
                ],
                [
                    1,
                    7,
                    8
                ],
                [
                    2,
                    7,
                    12
                ],
                [
                    3,
                    7,
                    7
                ],
                [
                    0,
                    8,
                    8
                ],
                [
                    1,
                    8,
                    1
                ],
                [
                    2,
                    8,
                    2
                ],
                [
                    3,
                    8,
                    6
                ],
                [
                    0,
                    9,
                    10
                ],
                [
                    1,
                    9,
                    4
                ],
                [
                    2,
                    9,
                    9
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
                    5
                ],
                [
                    3,
                    10,
                    11
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
                    11
                ],
                [
                    3,
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

---

## 📊 Position Breakdowns By Week

### QB
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
            12
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
            "90s",
            "BTE",
            "JST",
            "HMB",
            "KTT",
            "RRT",
            "TIB",
            "TOM",
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
                    4,
                    0,
                    6
                ],
                [
                    5,
                    0,
                    5
                ],
                [
                    6,
                    0,
                    8
                ],
                [
                    7,
                    0,
                    12
                ],
                [
                    8,
                    0,
                    7
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
                    4
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
                    5,
                    1,
                    10
                ],
                [
                    6,
                    1,
                    11
                ],
                [
                    7,
                    1,
                    3
                ],
                [
                    8,
                    1,
                    2
                ],
                [
                    9,
                    1,
                    9
                ],
                [
                    10,
                    1,
                    7
                ],
                [
                    11,
                    1,
                    8
                ],
                [
                    0,
                    2,
                    12
                ],
                [
                    1,
                    2,
                    4
                ],
                [
                    2,
                    2,
                    8
                ],
                [
                    3,
                    2,
                    5
                ],
                [
                    4,
                    2,
                    4
                ],
                [
                    5,
                    2,
                    12
                ],
                [
                    6,
                    2,
                    7
                ],
                [
                    7,
                    2,
                    8
                ],
                [
                    8,
                    2,
                    12
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
                    10
                ],
                [
                    2,
                    3,
                    10
                ],
                [
                    3,
                    3,
                    12
                ],
                [
                    4,
                    3,
                    8
                ],
                [
                    5,
                    3,
                    6
                ],
                [
                    6,
                    3,
                    2
                ],
                [
                    7,
                    3,
                    4
                ],
                [
                    8,
                    3,
                    3
                ],
                [
                    9,
                    3,
                    8
                ],
                [
                    10,
                    3,
                    10
                ],
                [
                    11,
                    3,
                    11
                ],
                [
                    0,
                    4,
                    3
                ],
                [
                    1,
                    4,
                    8
                ],
                [
                    2,
                    4,
                    1
                ],
                [
                    3,
                    4,
                    11
                ],
                [
                    4,
                    4,
                    9
                ],
                [
                    5,
                    4,
                    9
                ],
                [
                    6,
                    4,
                    12
                ],
                [
                    7,
                    4,
                    7
                ],
                [
                    8,
                    4,
                    5
                ],
                [
                    9,
                    4,
                    4
                ],
                [
                    10,
                    4,
                    12
                ],
                [
                    11,
                    4,
                    3
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
                    9
                ],
                [
                    3,
                    5,
                    2
                ],
                [
                    4,
                    5,
                    7
                ],
                [
                    5,
                    5,
                    8
                ],
                [
                    6,
                    5,
                    5
                ],
                [
                    7,
                    5,
                    1
                ],
                [
                    8,
                    5,
                    11
                ],
                [
                    9,
                    5,
                    11
                ],
                [
                    10,
                    5,
                    4
                ],
                [
                    11,
                    5,
                    12
                ],
                [
                    0,
                    6,
                    4
                ],
                [
                    1,
                    6,
                    5
                ],
                [
                    2,
                    6,
                    7
                ],
                [
                    3,
                    6,
                    6
                ],
                [
                    4,
                    6,
                    2
                ],
                [
                    5,
                    6,
                    3
                ],
                [
                    6,
                    6,
                    9
                ],
                [
                    7,
                    6,
                    5
                ],
                [
                    8,
                    6,
                    9
                ],
                [
                    9,
                    6,
                    12
                ],
                [
                    10,
                    6,
                    8
                ],
                [
                    11,
                    6,
                    10
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
                    5,
                    7,
                    7
                ],
                [
                    6,
                    7,
                    9
                ],
                [
                    7,
                    7,
                    10
                ],
                [
                    8,
                    7,
                    1
                ],
                [
                    9,
                    7,
                    6
                ],
                [
                    10,
                    7,
                    11
                ],
                [
                    11,
                    7,
                    5
                ],
                [
                    0,
                    8,
                    1
                ],
                [
                    1,
                    8,
                    11
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
                    5
                ],
                [
                    5,
                    8,
                    11
                ],
                [
                    6,
                    8,
                    6
                ],
                [
                    7,
                    8,
                    9
                ],
                [
                    8,
                    8,
                    6
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
                    9
                ],
                [
                    0,
                    9,
                    7
                ],
                [
                    1,
                    9,
                    1
                ],
                [
                    2,
                    9,
                    11
                ],
                [
                    3,
                    9,
                    8
                ],
                [
                    4,
                    9,
                    10
                ],
                [
                    5,
                    9,
                    4
                ],
                [
                    6,
                    9,
                    4
                ],
                [
                    7,
                    9,
                    6
                ],
                [
                    8,
                    9,
                    4
                ],
                [
                    9,
                    9,
                    2
                ],
                [
                    10,
                    9,
                    1
                ],
                [
                    11,
                    9,
                    2
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
                    4,
                    10,
                    3
                ],
                [
                    5,
                    10,
                    2
                ],
                [
                    6,
                    10,
                    3
                ],
                [
                    7,
                    10,
                    11
                ],
                [
                    8,
                    10,
                    10
                ],
                [
                    9,
                    10,
                    10
                ],
                [
                    10,
                    10,
                    2
                ],
                [
                    11,
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
                ],
                [
                    4,
                    11,
                    11
                ],
                [
                    5,
                    11,
                    1
                ],
                [
                    6,
                    11,
                    1
                ],
                [
                    7,
                    11,
                    2
                ],
                [
                    8,
                    11,
                    8
                ],
                [
                    9,
                    11,
                    5
                ],
                [
                    10,
                    11,
                    3
                ],
                [
                    11,
                    11,
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
```

### RB
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
            12
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
            "EET",
            "BTE",
            "HMB",
            "KTT",
            "MMT",
            "JST",
            "TIB",
            "TOM",
            "90s",
            "RRT",
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
                    3
                ],
                [
                    1,
                    0,
                    6
                ],
                [
                    2,
                    0,
                    3
                ],
                [
                    3,
                    0,
                    9
                ],
                [
                    4,
                    0,
                    11
                ],
                [
                    5,
                    0,
                    3
                ],
                [
                    6,
                    0,
                    12
                ],
                [
                    7,
                    0,
                    6
                ],
                [
                    8,
                    0,
                    11
                ],
                [
                    9,
                    0,
                    12
                ],
                [
                    10,
                    0,
                    12
                ],
                [
                    11,
                    0,
                    10
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
                    2,
                    1,
                    9
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
                    5,
                    1,
                    7
                ],
                [
                    6,
                    1,
                    6
                ],
                [
                    7,
                    1,
                    12
                ],
                [
                    8,
                    1,
                    3
                ],
                [
                    9,
                    1,
                    3
                ],
                [
                    10,
                    1,
                    5
                ],
                [
                    11,
                    1,
                    9
                ],
                [
                    0,
                    2,
                    12
                ],
                [
                    1,
                    2,
                    12
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
                    2
                ],
                [
                    7,
                    2,
                    9
                ],
                [
                    8,
                    2,
                    8
                ],
                [
                    9,
                    2,
                    7
                ],
                [
                    10,
                    2,
                    8
                ],
                [
                    11,
                    2,
                    7
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
                    11
                ],
                [
                    7,
                    3,
                    10
                ],
                [
                    8,
                    3,
                    2
                ],
                [
                    9,
                    3,
                    11
                ],
                [
                    10,
                    3,
                    2
                ],
                [
                    11,
                    3,
                    3
                ],
                [
                    0,
                    4,
                    8
                ],
                [
                    1,
                    4,
                    9
                ],
                [
                    2,
                    4,
                    12
                ],
                [
                    3,
                    4,
                    5
                ],
                [
                    4,
                    4,
                    7
                ],
                [
                    5,
                    4,
                    8
                ],
                [
                    6,
                    4,
                    4
                ],
                [
                    7,
                    4,
                    5
                ],
                [
                    8,
                    4,
                    12
                ],
                [
                    9,
                    4,
                    1
                ],
                [
                    10,
                    4,
                    7
                ],
                [
                    11,
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
                    10
                ],
                [
                    3,
                    5,
                    8
                ],
                [
                    4,
                    5,
                    9
                ],
                [
                    5,
                    5,
                    4
                ],
                [
                    6,
                    5,
                    10
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
                    2
                ],
                [
                    10,
                    5,
                    9
                ],
                [
                    11,
                    5,
                    8
                ],
                [
                    0,
                    6,
                    6
                ],
                [
                    1,
                    6,
                    5
                ],
                [
                    2,
                    6,
                    8
                ],
                [
                    3,
                    6,
                    3
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
                    12
                ],
                [
                    0,
                    7,
                    5
                ],
                [
                    1,
                    7,
                    1
                ],
                [
                    2,
                    7,
                    11
                ],
                [
                    3,
                    7,
                    11
                ],
                [
                    4,
                    7,
                    4
                ],
                [
                    5,
                    7,
                    6
                ],
                [
                    6,
                    7,
                    3
                ],
                [
                    7,
                    7,
                    1
                ],
                [
                    8,
                    7,
                    5
                ],
                [
                    9,
                    7,
                    9
                ],
                [
                    10,
                    7,
                    4
                ],
                [
                    11,
                    7,
                    11
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
                    5,
                    8,
                    11
                ],
                [
                    6,
                    8,
                    7
                ],
                [
                    7,
                    8,
                    2
                ],
                [
                    8,
                    8,
                    6
                ],
                [
                    9,
                    8,
                    6
                ],
                [
                    10,
                    8,
                    6
                ],
                [
                    11,
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
                    1
                ],
                [
                    3,
                    9,
                    1
                ],
                [
                    4,
                    9,
                    2
                ],
                [
                    5,
                    9,
                    12
                ],
                [
                    6,
                    9,
                    1
                ],
                [
                    7,
                    9,
                    8
                ],
                [
                    8,
                    9,
                    9
                ],
                [
                    9,
                    9,
                    5
                ],
                [
                    10,
                    9,
                    11
                ],
                [
                    11,
                    9,
                    4
                ],
                [
                    0,
                    10,
                    10
                ],
                [
                    1,
                    10,
                    2
                ],
                [
                    2,
                    10,
                    6
                ],
                [
                    3,
                    10,
                    2
                ],
                [
                    4,
                    10,
                    6
                ],
                [
                    5,
                    10,
                    5
                ],
                [
                    6,
                    10,
                    9
                ],
                [
                    7,
                    10,
                    11
                ],
                [
                    8,
                    10,
                    1
                ],
                [
                    9,
                    10,
                    7
                ],
                [
                    10,
                    10,
                    3
                ],
                [
                    11,
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
                ],
                [
                    5,
                    11,
                    1
                ],
                [
                    6,
                    11,
                    5
                ],
                [
                    7,
                    11,
                    6
                ],
                [
                    8,
                    11,
                    7
                ],
                [
                    9,
                    11,
                    10
                ],
                [
                    10,
                    11,
                    1
                ],
                [
                    11,
                    11,
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

### WR
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
            12
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
            "EET",
            "TIB",
            "TTC",
            "BTE",
            "KTT",
            "HMB",
            "90s",
            "MMT",
            "JST",
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
                    10
                ],
                [
                    1,
                    0,
                    12
                ],
                [
                    2,
                    0,
                    10
                ],
                [
                    3,
                    0,
                    1
                ],
                [
                    4,
                    0,
                    12
                ],
                [
                    5,
                    0,
                    9
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
                    12
                ],
                [
                    9,
                    0,
                    11
                ],
                [
                    10,
                    0,
                    6
                ],
                [
                    11,
                    0,
                    6
                ],
                [
                    0,
                    1,
                    4
                ],
                [
                    1,
                    1,
                    9
                ],
                [
                    2,
                    1,
                    6
                ],
                [
                    3,
                    1,
                    4
                ],
                [
                    4,
                    1,
                    9
                ],
                [
                    5,
                    1,
                    5
                ],
                [
                    6,
                    1,
                    9
                ],
                [
                    7,
                    1,
                    12
                ],
                [
                    8,
                    1,
                    4
                ],
                [
                    9,
                    1,
                    9
                ],
                [
                    10,
                    1,
                    10
                ],
                [
                    11,
                    1,
                    12
                ],
                [
                    0,
                    2,
                    3
                ],
                [
                    1,
                    2,
                    11
                ],
                [
                    2,
                    2,
                    10
                ],
                [
                    3,
                    2,
                    2
                ],
                [
                    4,
                    2,
                    10
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
                    8
                ],
                [
                    10,
                    2,
                    12
                ],
                [
                    11,
                    2,
                    3
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
                    9
                ],
                [
                    3,
                    3,
                    11
                ],
                [
                    4,
                    3,
                    11
                ],
                [
                    5,
                    3,
                    7
                ],
                [
                    6,
                    3,
                    8
                ],
                [
                    7,
                    3,
                    6
                ],
                [
                    8,
                    3,
                    3
                ],
                [
                    9,
                    3,
                    5
                ],
                [
                    10,
                    3,
                    3
                ],
                [
                    11,
                    3,
                    10
                ],
                [
                    0,
                    4,
                    9
                ],
                [
                    1,
                    4,
                    7
                ],
                [
                    2,
                    4,
                    8
                ],
                [
                    3,
                    4,
                    12
                ],
                [
                    4,
                    4,
                    7
                ],
                [
                    5,
                    4,
                    2
                ],
                [
                    6,
                    4,
                    10
                ],
                [
                    7,
                    4,
                    5
                ],
                [
                    8,
                    4,
                    6
                ],
                [
                    9,
                    4,
                    4
                ],
                [
                    10,
                    4,
                    7
                ],
                [
                    11,
                    4,
                    5
                ],
                [
                    0,
                    5,
                    8
                ],
                [
                    1,
                    5,
                    6
                ],
                [
                    2,
                    5,
                    12
                ],
                [
                    3,
                    5,
                    6
                ],
                [
                    4,
                    5,
                    8
                ],
                [
                    5,
                    5,
                    11
                ],
                [
                    6,
                    5,
                    3
                ],
                [
                    7,
                    5,
                    1
                ],
                [
                    8,
                    5,
                    5
                ],
                [
                    9,
                    5,
                    6
                ],
                [
                    10,
                    5,
                    4
                ],
                [
                    11,
                    5,
                    11
                ],
                [
                    0,
                    6,
                    1
                ],
                [
                    1,
                    6,
                    3
                ],
                [
                    2,
                    6,
                    3
                ],
                [
                    3,
                    6,
                    10
                ],
                [
                    4,
                    6,
                    5
                ],
                [
                    5,
                    6,
                    4
                ],
                [
                    6,
                    6,
                    11
                ],
                [
                    7,
                    6,
                    11
                ],
                [
                    8,
                    6,
                    11
                ],
                [
                    9,
                    6,
                    3
                ],
                [
                    10,
                    6,
                    9
                ],
                [
                    11,
                    6,
                    9
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
                    5,
                    7,
                    12
                ],
                [
                    6,
                    7,
                    12
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
                    2
                ],
                [
                    10,
                    7,
                    5
                ],
                [
                    11,
                    7,
                    1
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
                    5,
                    8,
                    5
                ],
                [
                    6,
                    8,
                    5
                ],
                [
                    7,
                    8,
                    2
                ],
                [
                    8,
                    8,
                    7
                ],
                [
                    9,
                    8,
                    10
                ],
                [
                    10,
                    8,
                    11
                ],
                [
                    11,
                    8,
                    4
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
                    2,
                    9,
                    5
                ],
                [
                    3,
                    9,
                    8
                ],
                [
                    4,
                    9,
                    6
                ],
                [
                    5,
                    9,
                    3
                ],
                [
                    6,
                    9,
                    1
                ],
                [
                    7,
                    9,
                    4
                ],
                [
                    8,
                    9,
                    9
                ],
                [
                    9,
                    9,
                    1
                ],
                [
                    10,
                    9,
                    7
                ],
                [
                    11,
                    9,
                    7
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
                    5,
                    10,
                    1
                ],
                [
                    6,
                    10,
                    2
                ],
                [
                    7,
                    10,
                    7
                ],
                [
                    8,
                    10,
                    1
                ],
                [
                    9,
                    10,
                    12
                ],
                [
                    10,
                    10,
                    2
                ],
                [
                    11,
                    10,
                    8
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
                ],
                [
                    5,
                    11,
                    10
                ],
                [
                    6,
                    11,
                    3
                ],
                [
                    7,
                    11,
                    9
                ],
                [
                    8,
                    11,
                    2
                ],
                [
                    9,
                    11,
                    6
                ],
                [
                    10,
                    11,
                    1
                ],
                [
                    11,
                    11,
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

### TE
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
            12
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
            "TIB",
            "ARV",
            "MMT",
            "EET",
            "TTC",
            "JST",
            "BTE",
            "TOM",
            "HMB",
            "90s",
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
                    9
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
                    12
                ],
                [
                    4,
                    0,
                    4
                ],
                [
                    5,
                    0,
                    11
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
                    12
                ],
                [
                    9,
                    0,
                    10
                ],
                [
                    10,
                    0,
                    6
                ],
                [
                    11,
                    0,
                    12
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
                    5,
                    1,
                    10
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
                    8
                ],
                [
                    9,
                    1,
                    3
                ],
                [
                    10,
                    1,
                    7
                ],
                [
                    11,
                    1,
                    5
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
                    2,
                    2,
                    12
                ],
                [
                    3,
                    2,
                    11
                ],
                [
                    4,
                    2,
                    8
                ],
                [
                    5,
                    2,
                    9
                ],
                [
                    6,
                    2,
                    5
                ],
                [
                    7,
                    2,
                    7
                ],
                [
                    8,
                    2,
                    2
                ],
                [
                    9,
                    2,
                    2
                ],
                [
                    10,
                    2,
                    8
                ],
                [
                    11,
                    2,
                    9
                ],
                [
                    0,
                    3,
                    10
                ],
                [
                    1,
                    3,
                    10
                ],
                [
                    2,
                    3,
                    1
                ],
                [
                    3,
                    3,
                    2
                ],
                [
                    4,
                    3,
                    1
                ],
                [
                    5,
                    3,
                    6
                ],
                [
                    6,
                    3,
                    9
                ],
                [
                    7,
                    3,
                    12
                ],
                [
                    8,
                    3,
                    9
                ],
                [
                    9,
                    3,
                    11
                ],
                [
                    10,
                    3,
                    9
                ],
                [
                    11,
                    3,
                    6
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
                    2,
                    4,
                    9
                ],
                [
                    3,
                    4,
                    9
                ],
                [
                    4,
                    4,
                    12
                ],
                [
                    5,
                    4,
                    3
                ],
                [
                    6,
                    4,
                    4
                ],
                [
                    7,
                    4,
                    9
                ],
                [
                    8,
                    4,
                    7
                ],
                [
                    9,
                    4,
                    5
                ],
                [
                    10,
                    4,
                    5
                ],
                [
                    11,
                    4,
                    3
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
                    4,
                    5,
                    3
                ],
                [
                    5,
                    5,
                    12
                ],
                [
                    6,
                    5,
                    12
                ],
                [
                    7,
                    5,
                    4
                ],
                [
                    8,
                    5,
                    5
                ],
                [
                    9,
                    5,
                    8
                ],
                [
                    10,
                    5,
                    11
                ],
                [
                    11,
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
                    11
                ],
                [
                    3,
                    6,
                    6
                ],
                [
                    4,
                    6,
                    10
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
                    2
                ],
                [
                    8,
                    6,
                    6
                ],
                [
                    9,
                    6,
                    12
                ],
                [
                    10,
                    6,
                    4
                ],
                [
                    11,
                    6,
                    8
                ],
                [
                    0,
                    7,
                    6
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
                    10
                ],
                [
                    4,
                    7,
                    6
                ],
                [
                    5,
                    7,
                    1
                ],
                [
                    6,
                    7,
                    10
                ],
                [
                    7,
                    7,
                    6
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
                    10
                ],
                [
                    11,
                    7,
                    7
                ],
                [
                    0,
                    8,
                    2
                ],
                [
                    1,
                    8,
                    3
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
                    7
                ],
                [
                    5,
                    8,
                    7
                ],
                [
                    6,
                    8,
                    2
                ],
                [
                    7,
                    8,
                    11
                ],
                [
                    8,
                    8,
                    10
                ],
                [
                    9,
                    8,
                    7
                ],
                [
                    10,
                    8,
                    2
                ],
                [
                    11,
                    8,
                    10
                ],
                [
                    0,
                    9,
                    7
                ],
                [
                    1,
                    9,
                    1
                ],
                [
                    2,
                    9,
                    8
                ],
                [
                    3,
                    9,
                    4
                ],
                [
                    4,
                    9,
                    2
                ],
                [
                    5,
                    9,
                    5
                ],
                [
                    6,
                    9,
                    3
                ],
                [
                    7,
                    9,
                    1
                ],
                [
                    8,
                    9,
                    11
                ],
                [
                    9,
                    9,
                    4
                ],
                [
                    10,
                    9,
                    12
                ],
                [
                    11,
                    9,
                    11
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
                    2,
                    10,
                    5
                ],
                [
                    3,
                    10,
                    7
                ],
                [
                    4,
                    10,
                    5
                ],
                [
                    5,
                    10,
                    8
                ],
                [
                    6,
                    10,
                    11
                ],
                [
                    7,
                    10,
                    3
                ],
                [
                    8,
                    10,
                    1
                ],
                [
                    9,
                    10,
                    9
                ],
                [
                    10,
                    10,
                    3
                ],
                [
                    11,
                    10,
                    4
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
                ],
                [
                    5,
                    11,
                    2
                ],
                [
                    6,
                    11,
                    1
                ],
                [
                    7,
                    11,
                    10
                ],
                [
                    8,
                    11,
                    3
                ],
                [
                    9,
                    11,
                    1
                ],
                [
                    10,
                    11,
                    1
                ],
                [
                    11,
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

---

## 🔬 Advanced Analytics

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
            "MMT",
            "RRT",
            "TTC",
            "HMB",
            "ARV",
            "JST",
            "TOM",
            "KTT",
            "90s",
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
            "Week 5",
            "Week 6",
            "Week 7",
            "Week 8",
            "Week 9",
            "Week 10",
            "Week 11",
            "Week 12"
        ]
    },
    "yAxis": {
        "type": "value",
        "name": "Efficiency %"
    },
    "series": [
        {
            "name": "MMT",
            "type": "line",
            "data": [
                75.5,
                86.5,
                92.7,
                78.0,
                89.2,
                91.9,
                95.5,
                87.2,
                93.6,
                83.1,
                82.6,
                94.9
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
                97.2,
                88.9,
                89.9,
                100.0,
                93.0,
                85.0,
                83.6,
                93.6
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
                99.8,
                96.5,
                96.1,
                84.8,
                82.3,
                100.0,
                83.4,
                96.0
            ]
        },
        {
            "name": "HMB",
            "type": "line",
            "data": [
                92.6,
                85.2,
                86.9,
                83.0,
                87.9,
                93.4,
                85.7,
                89.2,
                91.8,
                97.2,
                80.5,
                82.7
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
                98.2,
                98.6,
                91.7,
                89.7,
                98.7,
                81.8,
                87.0,
                80.2
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
                100.0,
                98.3,
                81.9,
                95.0,
                95.6,
                84.0,
                71.0,
                87.1
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
                88.2,
                87.1,
                86.4,
                99.6,
                79.5,
                98.1,
                96.0,
                88.0
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
                95.1,
                92.6,
                65.9,
                90.6,
                98.1,
                83.5,
                97.7,
                100.0
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
                91.9,
                72.5,
                78.0,
                85.1,
                86.4,
                83.1,
                56.3,
                78.2
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
                98.9,
                88.8,
                84.6,
                89.1,
                95.4,
                71.2,
                94.9,
                85.3
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
                100.0,
                90.6,
                72.7,
                100.0,
                88.3,
                74.8,
                77.3,
                79.4
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
                95.8,
                77.9,
                100.0,
                77.8,
                93.5,
                74.5,
                84.6,
                96.9
            ]
        }
    ],
    "grid": {
        "right": "10%",
        "left": "5%"
    }
}
```

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
            "name": "Michael's Managable Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        4.9,
                        -0.3,
                        2.2,
                        0.0
                    ],
                    "name": "Michael's Managable Team"
                }
            ]
        },
        {
            "name": "Americas Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        1.4,
                        -1.2,
                        2.4,
                        4.2
                    ],
                    "name": "Americas Team"
                }
            ]
        },
        {
            "name": "Third Time's the Charm?",
            "type": "radar",
            "data": [
                {
                    "value": [
                        4.8,
                        1.5,
                        -2.2,
                        -1.6
                    ],
                    "name": "Third Time's the Charm?"
                }
            ]
        },
        {
            "name": "Game of Zones - House Hamlin",
            "type": "radar",
            "data": [
                {
                    "value": [
                        4.8,
                        -2.6,
                        1.6,
                        2.3
                    ],
                    "name": "Game of Zones - House Hamlin"
                }
            ]
        },
        {
            "name": "Abbey's TNT Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -3.5,
                        1.4,
                        2.1,
                        -2.7
                    ],
                    "name": "Abbey's TNT Team"
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
                        2.8,
                        0.6,
                        0.5
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
                        -0.2,
                        0.4,
                        -2.2,
                        1.7
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
                        -0.8,
                        -1.4,
                        -1.5,
                        -2.9
                    ],
                    "name": "Mcconky Donkeys"
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
                        3.6,
                        -0.1,
                        2.1
                    ],
                    "name": "90s MonCon"
                }
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -3.7,
                        2.0,
                        -0.4,
                        -3.0
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
                        -4.6,
                        -2.9,
                        -2.4,
                        0.6
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
                        -7.1,
                        -3.2,
                        -0.9,
                        -2.8
                    ],
                    "name": "Emma's Excellent Team"
                }
            ]
        }
    ]
}
```
