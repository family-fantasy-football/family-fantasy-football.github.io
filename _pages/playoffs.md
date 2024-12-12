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
                  "name": "Pink Pony Club",
                  "value": "169.2",
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
                  "name": "Tom and Jerry",
                  "value": "154.4",
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
                  "name": "Hamlin My Business ",
                  "value": "144.36",
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
                  "name": "Who Killed Charbonnet Ramsey?",
                  "value": "168.3",
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