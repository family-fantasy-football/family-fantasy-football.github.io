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
          "name": "Champion",
          "symbol": "rect",
          "symbolSize": [250, 50],
          "children": [
            {
              "name": "Pink Pony Club",
              "value": "0.0",
              "itemStyle": {
                "color": "#7EC8B6"
              },
              "symbol": "rect",
              "symbolSize": [250, 50],
              "label": {
                "formatter": "{b}\n{c}"
              },
              "children": [
                {
                  "name": "Pink Pony Club",
                  "value": "366.24",
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
                  "value": "307.18",
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
              "name": "Who Killed Charbonnet Ramsey?",
              "value": "0.0",
              "itemStyle": {
                "color": "#1E90FF"
              },
              "symbol": "rect",
              "symbolSize": [250, 50],
              "label": {
                "formatter": "{b}\n{c}" },
              "children": [
                {
                  "name": "Hamlin My Business ",
                  "value": "244.28",
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
                  "value": "273.34",
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