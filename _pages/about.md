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

<div style="text-align: center; padding: 40px 0 30px 0;">
  <p style="font-size: 20px; color: #555; font-weight: 500;">2025-26 Season</p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">
  <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">🏆 Top Scorer</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Cathy Dickson and Jordan Dickson</div>
    <div style="font-size: 18px; opacity: 0.95;">805.74 points</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">📉 Bottom Scorer</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Christine Hamlin</div>
    <div style="font-size: 18px; opacity: 0.95;">550.11 points</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">🔥 Highest Week</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Ryan Ratcliff</div>
    <div style="font-size: 18px; opacity: 0.95;">178.27 pts (Week 5)</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">❄️ Lowest Week</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Nick Hill</div>
    <div style="font-size: 18px; opacity: 0.95;">65.20 pts (Week 6)</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: #2c3e50;">
    <div style="font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">🍀 Luckiest</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Kayden Mullins</div>
    <div style="font-size: 18px;">+1.4 wins vs expected</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: #2c3e50;">
    <div style="font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">😢 Unluckiest</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Cathy Dickson and Jordan Dickson</div>
    <div style="font-size: 18px;">-1.4 wins vs expected</div>
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
            6
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
                7,
                4,
                3,
                1,
                3,
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
            "name": "Abbey's TNT Team",
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
                4,
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
            "name": "Americas Team",
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
                12,
                10,
                10,
                10,
                8,
                6
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
                "color": "#17becf"
            },
            "itemStyle": {
                "color": "#17becf"
            },
            "data": [
                11,
                12,
                12,
                12,
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
                11,
                11,
                11,
                12,
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
                "color": "#ffbb78"
            },
            "itemStyle": {
                "color": "#ffbb78"
            },
            "data": [
                1,
                1,
                1,
                2,
                1,
                3
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
                9,
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
                "color": "#d62728"
            },
            "itemStyle": {
                "color": "#d62728"
            },
            "data": [
                10,
                9,
                7,
                9,
                7,
                5
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
                "color": "#aec7e8"
            },
            "itemStyle": {
                "color": "#aec7e8"
            },
            "data": [
                5,
                2,
                2,
                3,
                4,
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
                "color": "#c49c94"
            },
            "itemStyle": {
                "color": "#c49c94"
            },
            "data": [
                9,
                7,
                9,
                7,
                6,
                8
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
                "color": "#1f77b4"
            },
            "itemStyle": {
                "color": "#1f77b4"
            },
            "data": [
                6,
                3,
                6,
                5,
                2,
                1
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
        "min": 400.0,
        "max": 997.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": 400.0,
        "max": 997.0
    },
    "series": [
        {
            "name": "Third Time's the Charm?",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    791.29,
                    697.61
                ]
            ]
        },
        {
            "name": "90s MonCon",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    782.49,
                    680.98
                ]
            ]
        },
        {
            "name": "Rookie Mistake",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    715.53,
                    688.19
                ]
            ]
        },
        {
            "name": "Americas Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    787.87,
                    749.88
                ]
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    790.6,
                    714.91
                ]
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    659.07,
                    752.63
                ]
            ]
        },
        {
            "name": "Mcconky Donkeys",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    659.07,
                    611.28
                ]
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    805.74,
                    822.33
                ]
            ]
        },
        {
            "name": "Abbey's TNT Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    749.53,
                    702.84
                ]
            ]
        },
        {
            "name": "Game of Zones - House Hamlin",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    770.39,
                    669.17
                ]
            ]
        },
        {
            "name": "Emma's Excellent Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    550.59,
                    675.03
                ]
            ]
        },
        {
            "name": "Big Titi Energy",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    550.11,
                    847.43
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
                    400.0,
                    400.0
                ],
                [
                    997.0,
                    997.0
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
                        "xAxis": 717.69,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 717.69,
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
            "TTC",
            "MMT",
            "HMB",
            "ARV",
            "KTT",
            "RRT",
            "90s",
            "TOM",
            "JST",
            "TIB",
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
                    85.3,
                    107.57,
                    134.36,
                    163.3,
                    165.67
                ],
                [
                    111.95,
                    122.97,
                    134.52,
                    140.0,
                    148.67
                ],
                [
                    101.21,
                    116.14,
                    121.31,
                    132.15,
                    156.16
                ],
                [
                    97.27,
                    113.75,
                    117.95,
                    139.32,
                    157.57
                ],
                [
                    86.76,
                    91.25,
                    100.28,
                    122.64,
                    153.43
                ],
                [
                    80.1,
                    114.83,
                    134.68,
                    147.62,
                    178.27
                ],
                [
                    67.71,
                    112.58,
                    136.53,
                    158.9,
                    170.76
                ],
                [
                    94.53,
                    106.63,
                    117.96,
                    124.0,
                    150.05
                ],
                [
                    120.25,
                    124.35,
                    126.3,
                    145.6,
                    157.16
                ],
                [
                    65.2,
                    86.79,
                    121.82,
                    133.62,
                    137.55
                ],
                [
                    67.94,
                    77.63,
                    97.38,
                    105.83,
                    108.2
                ],
                [
                    73.65,
                    81.34,
                    82.06,
                    86.47,
                    94.17
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
                    106.14,
                    "TTC"
                ],
                [
                    0,
                    111.87,
                    "TTC"
                ],
                [
                    0,
                    85.3,
                    "TTC"
                ],
                [
                    0,
                    156.86,
                    "TTC"
                ],
                [
                    0,
                    165.45,
                    "TTC"
                ],
                [
                    0,
                    165.67,
                    "TTC"
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
                    148.67,
                    "MMT"
                ],
                [
                    1,
                    136.89,
                    "MMT"
                ],
                [
                    1,
                    119.91,
                    "MMT"
                ],
                [
                    1,
                    132.15,
                    "MMT"
                ],
                [
                    2,
                    176.38,
                    "HMB"
                ],
                [
                    2,
                    119.75,
                    "HMB"
                ],
                [
                    2,
                    114.94,
                    "HMB"
                ],
                [
                    2,
                    135.24,
                    "HMB"
                ],
                [
                    2,
                    122.87,
                    "HMB"
                ],
                [
                    2,
                    101.21,
                    "HMB"
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
                    145.7,
                    "ARV"
                ],
                [
                    3,
                    97.27,
                    "ARV"
                ],
                [
                    4,
                    101.15,
                    "KTT"
                ],
                [
                    4,
                    99.4,
                    "KTT"
                ],
                [
                    4,
                    88.53,
                    "KTT"
                ],
                [
                    4,
                    86.76,
                    "KTT"
                ],
                [
                    4,
                    129.8,
                    "KTT"
                ],
                [
                    4,
                    153.43,
                    "KTT"
                ],
                [
                    5,
                    80.1,
                    "RRT"
                ],
                [
                    5,
                    148.62,
                    "RRT"
                ],
                [
                    5,
                    144.61,
                    "RRT"
                ],
                [
                    5,
                    111.53,
                    "RRT"
                ],
                [
                    5,
                    178.27,
                    "RRT"
                ],
                [
                    5,
                    124.74,
                    "RRT"
                ],
                [
                    6,
                    111.47,
                    "90s"
                ],
                [
                    6,
                    157.15,
                    "90s"
                ],
                [
                    6,
                    170.76,
                    "90s"
                ],
                [
                    6,
                    115.91,
                    "90s"
                ],
                [
                    6,
                    159.49,
                    "90s"
                ],
                [
                    6,
                    67.71,
                    "90s"
                ],
                [
                    7,
                    103.67,
                    "TOM"
                ],
                [
                    7,
                    125.2,
                    "TOM"
                ],
                [
                    7,
                    94.53,
                    "TOM"
                ],
                [
                    7,
                    156.21,
                    "TOM"
                ],
                [
                    7,
                    120.4,
                    "TOM"
                ],
                [
                    7,
                    115.52,
                    "TOM"
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
                    8,
                    152.0,
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
                    9,
                    65.2,
                    "TIB"
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
                    105.14,
                    "EET"
                ],
                [
                    10,
                    89.62,
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
                    147.85,
                    "BTE"
                ],
                [
                    11,
                    87.79,
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
            "TTC",
            "MMT",
            "HMB",
            "ARV",
            "KTT",
            "RRT",
            "90s",
            "TOM",
            "JST",
            "TIB",
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
                    1
                ],
                [
                    1,
                    0,
                    5
                ],
                [
                    2,
                    0,
                    8
                ],
                [
                    3,
                    0,
                    11
                ],
                [
                    0,
                    1,
                    3
                ],
                [
                    1,
                    1,
                    8
                ],
                [
                    2,
                    1,
                    4
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
                    10
                ],
                [
                    2,
                    2,
                    3
                ],
                [
                    3,
                    2,
                    3
                ],
                [
                    0,
                    3,
                    10
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
                    1
                ],
                [
                    0,
                    4,
                    5
                ],
                [
                    1,
                    4,
                    9
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
                    7
                ],
                [
                    1,
                    6,
                    2
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
                    8
                ],
                [
                    1,
                    7,
                    6
                ],
                [
                    2,
                    7,
                    2
                ],
                [
                    3,
                    7,
                    10
                ],
                [
                    0,
                    8,
                    4
                ],
                [
                    1,
                    8,
                    3
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
                    9
                ],
                [
                    1,
                    9,
                    4
                ],
                [
                    2,
                    9,
                    12
                ],
                [
                    3,
                    9,
                    8
                ],
                [
                    0,
                    10,
                    12
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
                    11
                ],
                [
                    1,
                    11,
                    12
                ],
                [
                    2,
                    11,
                    5
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
            6
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
            "90s",
            "JST",
            "TOM",
            "TIB",
            "HMB",
            "RRT",
            "MMT",
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
                    6
                ],
                [
                    1,
                    0,
                    12
                ],
                [
                    2,
                    0,
                    2
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
                    5,
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
                    9
                ],
                [
                    2,
                    1,
                    12
                ],
                [
                    3,
                    1,
                    9
                ],
                [
                    4,
                    1,
                    6
                ],
                [
                    5,
                    1,
                    5
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
                    5,
                    2,
                    6
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
                    4,
                    3,
                    4
                ],
                [
                    5,
                    3,
                    12
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
                    4,
                    5,
                    10
                ],
                [
                    5,
                    5,
                    4
                ],
                [
                    0,
                    6,
                    1
                ],
                [
                    1,
                    6,
                    11
                ],
                [
                    2,
                    6,
                    6
                ],
                [
                    3,
                    6,
                    4
                ],
                [
                    4,
                    6,
                    5
                ],
                [
                    5,
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
                    4,
                    7,
                    7
                ],
                [
                    5,
                    7,
                    8
                ],
                [
                    0,
                    8,
                    10
                ],
                [
                    1,
                    8,
                    7
                ],
                [
                    2,
                    8,
                    4
                ],
                [
                    3,
                    8,
                    7
                ],
                [
                    4,
                    8,
                    1
                ],
                [
                    5,
                    8,
                    7
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
                    2,
                    9,
                    3
                ],
                [
                    3,
                    9,
                    3
                ],
                [
                    4,
                    9,
                    11
                ],
                [
                    5,
                    9,
                    1
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
                    5,
                    10,
                    3
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
                ],
                [
                    5,
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
            6
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
            "BTE",
            "KTT",
            "MMT",
            "TIB",
            "TOM",
            "ARV",
            "JST",
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
                    5,
                    0,
                    7
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
                    5,
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
                    2,
                    3,
                    12
                ],
                [
                    3,
                    3,
                    5
                ],
                [
                    4,
                    3,
                    7
                ],
                [
                    5,
                    3,
                    8
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
                    5,
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
                    4,
                    6,
                    3
                ],
                [
                    5,
                    6,
                    11
                ],
                [
                    0,
                    7,
                    3
                ],
                [
                    1,
                    7,
                    6
                ],
                [
                    2,
                    7,
                    3
                ],
                [
                    3,
                    7,
                    9
                ],
                [
                    4,
                    7,
                    11
                ],
                [
                    5,
                    7,
                    3
                ],
                [
                    0,
                    8,
                    6
                ],
                [
                    1,
                    8,
                    5
                ],
                [
                    2,
                    8,
                    8
                ],
                [
                    3,
                    8,
                    3
                ],
                [
                    4,
                    8,
                    8
                ],
                [
                    5,
                    8,
                    2
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
                    5,
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
                    5,
                    10,
                    12
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
            6
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
            "TTC",
            "KTT",
            "BTE",
            "TIB",
            "90s",
            "EET",
            "JST",
            "MMT",
            "ARV",
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
                    4,
                    1,
                    11
                ],
                [
                    5,
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
                    6
                ],
                [
                    2,
                    2,
                    12
                ],
                [
                    3,
                    2,
                    6
                ],
                [
                    4,
                    2,
                    8
                ],
                [
                    5,
                    2,
                    11
                ],
                [
                    0,
                    3,
                    9
                ],
                [
                    1,
                    3,
                    7
                ],
                [
                    2,
                    3,
                    8
                ],
                [
                    3,
                    3,
                    12
                ],
                [
                    4,
                    3,
                    7
                ],
                [
                    5,
                    3,
                    2
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
                    5,
                    4,
                    8
                ],
                [
                    0,
                    5,
                    11
                ],
                [
                    1,
                    5,
                    1
                ],
                [
                    2,
                    5,
                    7
                ],
                [
                    3,
                    5,
                    9
                ],
                [
                    4,
                    5,
                    2
                ],
                [
                    5,
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
                    9
                ],
                [
                    2,
                    6,
                    6
                ],
                [
                    3,
                    6,
                    4
                ],
                [
                    4,
                    6,
                    9
                ],
                [
                    5,
                    6,
                    5
                ],
                [
                    0,
                    7,
                    7
                ],
                [
                    1,
                    7,
                    5
                ],
                [
                    2,
                    7,
                    5
                ],
                [
                    3,
                    7,
                    8
                ],
                [
                    4,
                    7,
                    6
                ],
                [
                    5,
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
                    0,
                    9,
                    2
                ],
                [
                    1,
                    9,
                    4
                ],
                [
                    2,
                    9,
                    4
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
                    10
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
                    4,
                    10,
                    5
                ],
                [
                    5,
                    10,
                    4
                ],
                [
                    0,
                    11,
                    12
                ],
                [
                    1,
                    11,
                    2
                ],
                [
                    2,
                    11,
                    1
                ],
                [
                    3,
                    11,
                    5
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
            6
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
            "TTC",
            "JST",
            "BTE",
            "90s",
            "MMT",
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
                    5,
                    0,
                    9
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
                    5,
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
                    5,
                    3,
                    11
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
                    3
                ],
                [
                    3,
                    4,
                    5
                ],
                [
                    4,
                    4,
                    3
                ],
                [
                    5,
                    4,
                    12
                ],
                [
                    0,
                    5,
                    3
                ],
                [
                    1,
                    5,
                    4
                ],
                [
                    2,
                    5,
                    11
                ],
                [
                    3,
                    5,
                    6
                ],
                [
                    4,
                    5,
                    10
                ],
                [
                    5,
                    5,
                    4
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
                    2,
                    6,
                    4
                ],
                [
                    3,
                    6,
                    10
                ],
                [
                    4,
                    6,
                    6
                ],
                [
                    5,
                    6,
                    1
                ],
                [
                    0,
                    7,
                    1
                ],
                [
                    1,
                    7,
                    5
                ],
                [
                    2,
                    7,
                    5
                ],
                [
                    3,
                    7,
                    7
                ],
                [
                    4,
                    7,
                    5
                ],
                [
                    5,
                    7,
                    8
                ],
                [
                    0,
                    8,
                    10
                ],
                [
                    1,
                    8,
                    10
                ],
                [
                    2,
                    8,
                    1
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
                    6
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
                    5,
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
                    5,
                    10,
                    5
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
            "TTC",
            "MMT",
            "HMB",
            "ARV",
            "KTT",
            "RRT",
            "90s",
            "TOM",
            "JST",
            "TIB",
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
            "Week 4",
            "Week 5",
            "Week 6"
        ]
    },
    "yAxis": {
        "type": "value",
        "name": "Efficiency %"
    },
    "series": [
        {
            "name": "TTC",
            "type": "line",
            "data": [
                90.7,
                85.5,
                91.1,
                88.4,
                99.8,
                96.5
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
                89.2,
                91.9
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
                93.4
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
                98.6
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
                92.6
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
                88.9
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
                72.5
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
                87.1
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
                98.3
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
                88.8
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
                77.9
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
                90.6
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
            "name": "Third Time's the Charm?",
            "type": "radar",
            "data": [
                {
                    "value": [
                        3.9,
                        0.6,
                        -3.2,
                        -0.3
                    ],
                    "name": "Third Time's the Charm?"
                }
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        4.0,
                        -0.6,
                        1.6,
                        0.6
                    ],
                    "name": "Michael's Managable Team"
                }
            ]
        },
        {
            "name": "Game of Zones - House Hamlin",
            "type": "radar",
            "data": [
                {
                    "value": [
                        5.5,
                        -1.8,
                        3.9,
                        2.5
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
                        -4.5,
                        3.6,
                        3.3,
                        -5.0
                    ],
                    "name": "Abbey's TNT Team"
                }
            ]
        },
        {
            "name": "Mcconky Donkeys",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.4,
                        -2.5,
                        -2.8,
                        -1.7
                    ],
                    "name": "Mcconky Donkeys"
                }
            ]
        },
        {
            "name": "Americas Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -0.3,
                        0.4,
                        0.7,
                        3.0
                    ],
                    "name": "Americas Team"
                }
            ]
        },
        {
            "name": "90s MonCon",
            "type": "radar",
            "data": [
                {
                    "value": [
                        3.2,
                        3.6,
                        0.3,
                        1.8
                    ],
                    "name": "90s MonCon"
                }
            ]
        },
        {
            "name": "Rookie Mistake",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -2.2,
                        1.0,
                        -2.5,
                        3.0
                    ],
                    "name": "Rookie Mistake"
                }
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "radar",
            "data": [
                {
                    "value": [
                        2.9,
                        2.5,
                        0.9,
                        1.0
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
                        -1.7,
                        1.6,
                        0.8,
                        -5.1
                    ],
                    "name": "To Infinity and Bijan!"
                }
            ]
        },
        {
            "name": "Emma's Excellent Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -6.6,
                        -3.1,
                        -0.4,
                        -2.9
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
                        -6.4,
                        -3.6,
                        -3.8,
                        0.7
                    ],
                    "name": "Big Titi Energy"
                }
            ]
        }
    ]
}
```
