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
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Michael Ratcliff</div>
    <div style="font-size: 18px; opacity: 0.95;">978.53 points</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">📉 Bottom Scorer</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Emma Grau</div>
    <div style="font-size: 18px; opacity: 0.95;">616.78 points</div>
  </div>
  
  <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); color: white;">
    <div style="font-size: 14px; opacity: 0.9; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">🔥 Highest Week</div>
    <div style="font-size: 24px; font-weight: 700; margin-bottom: 4px;">Michael Ratcliff</div>
    <div style="font-size: 18px; opacity: 0.95;">187.93 pts (Week 7)</div>
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
            6,
            7
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
                "color": "#c49c94"
            },
            "itemStyle": {
                "color": "#c49c94"
            },
            "data": [
                7,
                4,
                3,
                1,
                3,
                7,
                8
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
                "color": "#ffbb78"
            },
            "itemStyle": {
                "color": "#ffbb78"
            },
            "data": [
                4,
                8,
                5,
                4,
                5,
                4,
                3
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
                "color": "#98df8a"
            },
            "itemStyle": {
                "color": "#98df8a"
            },
            "data": [
                12,
                10,
                10,
                10,
                8,
                6,
                4
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
                "color": "#d62728"
            },
            "itemStyle": {
                "color": "#d62728"
            },
            "data": [
                1,
                1,
                1,
                2,
                1,
                3,
                5
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
                "color": "#8c564b"
            },
            "itemStyle": {
                "color": "#8c564b"
            },
            "data": [
                3,
                5,
                4,
                6,
                9,
                9,
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
            "name": "Mcconky Donkeys",
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
                7,
                9,
                7,
                5,
                6
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
                2,
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
                "color": "#f7b6d2"
            },
            "itemStyle": {
                "color": "#f7b6d2"
            },
            "data": [
                9,
                7,
                9,
                7,
                6,
                8,
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
                1,
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
        "min": 467.0,
        "max": 1139.0
    },
    "yAxis": {
        "type": "value",
        "name": "Points Against",
        "nameLocation": "middle",
        "nameGap": 40,
        "min": 467.0,
        "max": 1139.0
    },
    "series": [
        {
            "name": "Third Time's the Charm?",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    932.49,
                    793.5
                ]
            ]
        },
        {
            "name": "90s MonCon",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    880.38,
                    822.55
                ]
            ]
        },
        {
            "name": "Rookie Mistake",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    818.49,
                    861.29
                ]
            ]
        },
        {
            "name": "Americas Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    960.97,
                    852.84
                ]
            ]
        },
        {
            "name": "Michael's Managable Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    978.53,
                    781.1
                ]
            ]
        },
        {
            "name": "To Infinity and Bijan!",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    754.48,
                    843.79
                ]
            ]
        },
        {
            "name": "Mcconky Donkeys",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    746.58,
                    713.17
                ]
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    947.31,
                    920.22
                ]
            ]
        },
        {
            "name": "Abbey's TNT Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    851.42,
                    790.35
                ]
            ]
        },
        {
            "name": "Game of Zones - House Hamlin",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    861.55,
                    764.58
                ]
            ]
        },
        {
            "name": "Emma's Excellent Team",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    616.78,
                    862.96
                ]
            ]
        },
        {
            "name": "Big Titi Energy",
            "type": "scatter",
            "symbolSize": 15,
            "data": [
                [
                    646.0,
                    988.63
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
                    467.0,
                    467.0
                ],
                [
                    1139.0,
                    1139.0
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
                        "xAxis": 832.92,
                        "lineStyle": {
                            "color": "blue",
                            "opacity": 0.5
                        }
                    },
                    {
                        "yAxis": 832.92,
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
            "ARV",
            "RRT",
            "HMB",
            "KTT",
            "JST",
            "90s",
            "TOM",
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
                    85.3,
                    109.0,
                    141.2,
                    161.16,
                    165.67
                ],
                [
                    111.95,
                    126.03,
                    136.89,
                    144.85,
                    173.08
                ],
                [
                    97.27,
                    107.49,
                    115.72,
                    132.94,
                    157.57
                ],
                [
                    80.1,
                    118.14,
                    144.61,
                    160.86,
                    178.27
                ],
                [
                    91.16,
                    108.07,
                    119.75,
                    129.06,
                    160.53
                ],
                [
                    86.76,
                    88.02,
                    99.4,
                    115.48,
                    153.43
                ],
                [
                    120.25,
                    124.98,
                    126.38,
                    146.78,
                    157.16
                ],
                [
                    67.71,
                    104.68,
                    115.91,
                    158.32,
                    170.76
                ],
                [
                    94.53,
                    103.32,
                    115.52,
                    122.8,
                    152.03
                ],
                [
                    65.2,
                    87.0,
                    111.43,
                    133.16,
                    137.55
                ],
                [
                    69.1,
                    81.43,
                    82.52,
                    91.84,
                    107.46
                ],
                [
                    66.19,
                    70.78,
                    89.62,
                    105.6,
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
                    0,
                    141.2,
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
                    1,
                    187.93,
                    "MMT"
                ],
                [
                    2,
                    115.72,
                    "ARV"
                ],
                [
                    2,
                    113.09,
                    "ARV"
                ],
                [
                    2,
                    120.18,
                    "ARV"
                ],
                [
                    2,
                    157.57,
                    "ARV"
                ],
                [
                    2,
                    145.7,
                    "ARV"
                ],
                [
                    2,
                    97.27,
                    "ARV"
                ],
                [
                    2,
                    101.89,
                    "ARV"
                ],
                [
                    3,
                    80.1,
                    "RRT"
                ],
                [
                    3,
                    148.62,
                    "RRT"
                ],
                [
                    3,
                    144.61,
                    "RRT"
                ],
                [
                    3,
                    111.53,
                    "RRT"
                ],
                [
                    3,
                    178.27,
                    "RRT"
                ],
                [
                    3,
                    124.74,
                    "RRT"
                ],
                [
                    3,
                    173.1,
                    "RRT"
                ],
                [
                    4,
                    176.38,
                    "HMB"
                ],
                [
                    4,
                    119.75,
                    "HMB"
                ],
                [
                    4,
                    114.94,
                    "HMB"
                ],
                [
                    4,
                    135.24,
                    "HMB"
                ],
                [
                    4,
                    122.87,
                    "HMB"
                ],
                [
                    4,
                    101.21,
                    "HMB"
                ],
                [
                    4,
                    91.16,
                    "HMB"
                ],
                [
                    5,
                    101.15,
                    "KTT"
                ],
                [
                    5,
                    99.4,
                    "KTT"
                ],
                [
                    5,
                    88.53,
                    "KTT"
                ],
                [
                    5,
                    86.76,
                    "KTT"
                ],
                [
                    5,
                    129.8,
                    "KTT"
                ],
                [
                    5,
                    153.43,
                    "KTT"
                ],
                [
                    5,
                    87.51,
                    "KTT"
                ],
                [
                    6,
                    126.38,
                    "JST"
                ],
                [
                    6,
                    126.22,
                    "JST"
                ],
                [
                    6,
                    157.16,
                    "JST"
                ],
                [
                    6,
                    123.73,
                    "JST"
                ],
                [
                    6,
                    120.25,
                    "JST"
                ],
                [
                    6,
                    152.0,
                    "JST"
                ],
                [
                    6,
                    141.57,
                    "JST"
                ],
                [
                    7,
                    111.47,
                    "90s"
                ],
                [
                    7,
                    157.15,
                    "90s"
                ],
                [
                    7,
                    170.76,
                    "90s"
                ],
                [
                    7,
                    115.91,
                    "90s"
                ],
                [
                    7,
                    159.49,
                    "90s"
                ],
                [
                    7,
                    67.71,
                    "90s"
                ],
                [
                    7,
                    97.89,
                    "90s"
                ],
                [
                    8,
                    103.67,
                    "TOM"
                ],
                [
                    8,
                    125.2,
                    "TOM"
                ],
                [
                    8,
                    94.53,
                    "TOM"
                ],
                [
                    8,
                    156.21,
                    "TOM"
                ],
                [
                    8,
                    120.4,
                    "TOM"
                ],
                [
                    8,
                    115.52,
                    "TOM"
                ],
                [
                    8,
                    102.96,
                    "TOM"
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
            "ARV",
            "RRT",
            "HMB",
            "KTT",
            "JST",
            "90s",
            "TOM",
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
                    5
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
                    3
                ],
                [
                    3,
                    1,
                    2
                ],
                [
                    0,
                    2,
                    9
                ],
                [
                    1,
                    2,
                    4
                ],
                [
                    2,
                    2,
                    11
                ],
                [
                    3,
                    2,
                    3
                ],
                [
                    0,
                    3,
                    5
                ],
                [
                    1,
                    3,
                    8
                ],
                [
                    2,
                    3,
                    1
                ],
                [
                    3,
                    3,
                    1
                ],
                [
                    0,
                    4,
                    3
                ],
                [
                    1,
                    4,
                    10
                ],
                [
                    2,
                    4,
                    4
                ],
                [
                    3,
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
                    9
                ],
                [
                    2,
                    5,
                    8
                ],
                [
                    3,
                    5,
                    9
                ],
                [
                    0,
                    6,
                    4
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
                    7
                ],
                [
                    0,
                    8,
                    7
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
                    10
                ],
                [
                    0,
                    9,
                    11
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
            7
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
            "JST",
            "90s",
            "BTE",
            "RRT",
            "TOM",
            "TIB",
            "HMB",
            "KTT",
            "MMT",
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
                    6,
                    0,
                    11
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
                    6,
                    1,
                    8
                ],
                [
                    0,
                    2,
                    3
                ],
                [
                    1,
                    2,
                    8
                ],
                [
                    2,
                    2,
                    1
                ],
                [
                    3,
                    2,
                    11
                ],
                [
                    4,
                    2,
                    9
                ],
                [
                    5,
                    2,
                    9
                ],
                [
                    6,
                    2,
                    12
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
                    6,
                    3,
                    7
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
                    2,
                    4,
                    10
                ],
                [
                    3,
                    4,
                    12
                ],
                [
                    4,
                    4,
                    8
                ],
                [
                    5,
                    4,
                    6
                ],
                [
                    6,
                    4,
                    2
                ],
                [
                    0,
                    5,
                    10
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
                    7
                ],
                [
                    4,
                    5,
                    1
                ],
                [
                    5,
                    5,
                    7
                ],
                [
                    6,
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
                    8
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
                    11
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
                    5
                ],
                [
                    5,
                    7,
                    11
                ],
                [
                    6,
                    7,
                    6
                ],
                [
                    0,
                    8,
                    5
                ],
                [
                    1,
                    8,
                    6
                ],
                [
                    2,
                    8,
                    9
                ],
                [
                    3,
                    8,
                    2
                ],
                [
                    4,
                    8,
                    7
                ],
                [
                    5,
                    8,
                    8
                ],
                [
                    6,
                    8,
                    5
                ],
                [
                    0,
                    9,
                    4
                ],
                [
                    1,
                    9,
                    5
                ],
                [
                    2,
                    9,
                    7
                ],
                [
                    3,
                    9,
                    6
                ],
                [
                    4,
                    9,
                    2
                ],
                [
                    5,
                    9,
                    3
                ],
                [
                    6,
                    9,
                    9
                ],
                [
                    0,
                    10,
                    8
                ],
                [
                    1,
                    10,
                    2
                ],
                [
                    2,
                    10,
                    3
                ],
                [
                    3,
                    10,
                    3
                ],
                [
                    4,
                    10,
                    11
                ],
                [
                    5,
                    10,
                    1
                ],
                [
                    6,
                    10,
                    1
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
                ],
                [
                    6,
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
            7
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
            "MMT",
            "BTE",
            "ARV",
            "TOM",
            "TIB",
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
                    6,
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
                    6,
                    1,
                    11
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
                    5,
                    2,
                    8
                ],
                [
                    6,
                    2,
                    4
                ],
                [
                    0,
                    3,
                    7
                ],
                [
                    1,
                    3,
                    4
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
                    9
                ],
                [
                    5,
                    3,
                    4
                ],
                [
                    6,
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
                    12
                ],
                [
                    2,
                    4,
                    4
                ],
                [
                    3,
                    4,
                    6
                ],
                [
                    4,
                    4,
                    5
                ],
                [
                    5,
                    4,
                    10
                ],
                [
                    6,
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
                    5,
                    5,
                    3
                ],
                [
                    6,
                    5,
                    12
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
                    6,
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
                    6,
                    8,
                    8
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
                    6,
                    9,
                    9
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
                    6,
                    10,
                    1
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
            7
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
            "90s",
            "TIB",
            "EET",
            "HMB",
            "MMT",
            "JST",
            "ARV",
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
                    5,
                    0,
                    7
                ],
                [
                    6,
                    0,
                    8
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
                    5,
                    1,
                    9
                ],
                [
                    6,
                    1,
                    7
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
                    5,
                    2,
                    2
                ],
                [
                    6,
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
                    5,
                    3,
                    11
                ],
                [
                    6,
                    3,
                    3
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
                    4,
                    4,
                    2
                ],
                [
                    5,
                    4,
                    12
                ],
                [
                    6,
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
                    4,
                    5,
                    10
                ],
                [
                    5,
                    5,
                    8
                ],
                [
                    6,
                    5,
                    6
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
                    6,
                    6,
                    9
                ],
                [
                    0,
                    7,
                    1
                ],
                [
                    1,
                    7,
                    3
                ],
                [
                    2,
                    7,
                    3
                ],
                [
                    3,
                    7,
                    10
                ],
                [
                    4,
                    7,
                    5
                ],
                [
                    5,
                    7,
                    4
                ],
                [
                    6,
                    7,
                    11
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
                    2,
                    10,
                    4
                ],
                [
                    3,
                    10,
                    3
                ],
                [
                    4,
                    10,
                    3
                ],
                [
                    5,
                    10,
                    10
                ],
                [
                    6,
                    10,
                    3
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
                ],
                [
                    6,
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
            7
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
            "KTT",
            "EET",
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
                    12
                ],
                [
                    1,
                    0,
                    11
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
                    11
                ],
                [
                    5,
                    0,
                    10
                ],
                [
                    6,
                    0,
                    6
                ],
                [
                    0,
                    1,
                    11
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
                    11
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
                    5
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
                    6
                ],
                [
                    3,
                    2,
                    12
                ],
                [
                    4,
                    2,
                    4
                ],
                [
                    5,
                    2,
                    11
                ],
                [
                    6,
                    2,
                    7
                ],
                [
                    0,
                    3,
                    4
                ],
                [
                    1,
                    3,
                    12
                ],
                [
                    2,
                    3,
                    9
                ],
                [
                    3,
                    3,
                    9
                ],
                [
                    4,
                    3,
                    12
                ],
                [
                    5,
                    3,
                    3
                ],
                [
                    6,
                    3,
                    4
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
                    6,
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
                    6,
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
                    6,
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
                    6,
                    7,
                    11
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
                    6,
                    8,
                    9
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
                    6,
                    9,
                    2
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
                    6,
                    10,
                    3
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
            "ARV",
            "RRT",
            "HMB",
            "KTT",
            "JST",
            "90s",
            "TOM",
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
            "Week 7"
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
                96.5,
                96.1
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
                91.9,
                95.5
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
                91.7
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
                89.9
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
                85.7
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
                65.9
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
                81.9
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
                78.0
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
                86.4
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
                84.6
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
                72.7
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
                100.0
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
                        5.0,
                        0.9,
                        -3.0,
                        -0.8
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
                        4.4,
                        -0.5,
                        1.8,
                        1.0
                    ],
                    "name": "Michael's Managable Team"
                }
            ]
        },
        {
            "name": "Abbey's TNT Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        -4.3,
                        3.3,
                        3.0,
                        -4.6
                    ],
                    "name": "Abbey's TNT Team"
                }
            ]
        },
        {
            "name": "Americas Team",
            "type": "radar",
            "data": [
                {
                    "value": [
                        0.2,
                        -0.1,
                        1.5,
                        3.4
                    ],
                    "name": "Americas Team"
                }
            ]
        },
        {
            "name": "Game of Zones - House Hamlin",
            "type": "radar",
            "data": [
                {
                    "value": [
                        5.1,
                        -2.2,
                        3.3,
                        2.3
                    ],
                    "name": "Game of Zones - House Hamlin"
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
                        -2.3,
                        -2.6,
                        -1.8
                    ],
                    "name": "Mcconky Donkeys"
                }
            ]
        },
        {
            "name": "Mama Daughter Duo",
            "type": "radar",
            "data": [
                {
                    "value": [
                        2.7,
                        2.9,
                        0.9,
                        0.8
                    ],
                    "name": "Mama Daughter Duo"
                }
            ]
        },
        {
            "name": "90s MonCon",
            "type": "radar",
            "data": [
                {
                    "value": [
                        1.9,
                        3.8,
                        0.1,
                        1.2
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
                        -1.8,
                        0.6,
                        -2.4,
                        3.1
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
                        -2.6,
                        1.9,
                        0.4,
                        -4.9
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
                        -6.0,
                        -3.6,
                        -3.6,
                        0.7
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
                        -6.7,
                        -3.3,
                        -0.5,
                        -2.8
                    ],
                    "name": "Emma's Excellent Team"
                }
            ]
        }
    ]
}
```
