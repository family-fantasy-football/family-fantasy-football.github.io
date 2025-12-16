---
layout: page
permalink: /playoffs/
title: playoffs
description: 
nav: false
nav_order: 7
chart:
  echarts: true
---
<style>
  table[data-toggle="table"] tbody td {
    color: #2c3e50 !important;
  }
</style>

```echarts
{
  "series": [
    {
      "type": "tree",
      "data": [
        {
          "name": "Finals",
          "symbol": "rect",
          "symbolSize": [250, 50],
          "children": [
            {
              "name": "Winner of Semifinal 1",
              "symbol": "rect",
              "symbolSize": [250, 50],
              "children": [
                {
                  "name": "Americas Team",
                  "value": "147.92",
                  "itemStyle": {
                    "color": "#7EC8B6"
                  },
                  "symbol": "rect",
                  "symbolSize": [250, 50],
                  "label": {
                    "formatter": "{b}\n{c}"
                  }
                },
                {
                  "name": "Third Time's the Charm?",
                  "value": "98.77",
                  "itemStyle": {
                    "color": "#FF6347"
                  },
                  "symbol": "rect",
                  "symbolSize": [250, 50],
                  "label": {
                    "formatter": "{b}\n{c}"
                  }
                }
              ]
            },
            {
              "name": "Winner of Semifinal 2",
              "symbol": "rect",
              "symbolSize": [250, 50],
              "children": [
                {
                  "name": "Michael's Managable Team",
                  "value": "79.85",
                  "itemStyle": {
                    "color": "#FFD700"
                  },
                  "symbol": "rect",
                  "symbolSize": [250, 50],
                  "label": {
                    "formatter": "{b}\n{c}"
                  }
                },
                {
                  "name": "Abbey's TNT Team",
                  "value": "135.98",
                  "itemStyle": {
                    "color": "#1E90FF"
                  },
                  "symbol": "rect",
                  "symbolSize": [250, 50],
                  "label": {
                    "formatter": "{b}\n{c}"
                  }
                }
              ]
            }
          ]
        }
      ],
      "orient": "RL",
      "top": "5%",
      "left": "15%",
      "bottom": "5%",
      "right": "15%",
      "label": {
        "position": "inside",
        "verticalAlign": "middle",
        "align": "center",
        "fontSize": 16
      },
      "lineStyle": {
        "color": "#555",
        "width": 2
      }
    }
  ]
}
```