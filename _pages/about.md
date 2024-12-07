---
layout: page
title: home
permalink: /
# subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Motto. Etc.

profile:
  align: center
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info:

news: false # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false # includes social icons at the bottom of the page
pretty_table: True
chart:
  echarts: true
---

## Welcome to the site for the Family Fantasy Footbal League! It is clearly still under development

<div style="margin-bottom: 30px;">
  Your text here
</div>

### Current Standings:

<table
 data-click-to-select="true"
 data-height="690"
 data-pagination="true"
 data-search="false"
 data-toggle="table"
 data-url="{{ "/assets/json/standings.json"}}">
 <thead>
   <tr>
     <th data-field="team" data-halign="left" data-align="left" data-sortable="true">Team What</th>
     <th data-field="record" data-halign="center" data-align="center" data-sortable="true">Record</th>
     <th data-field="last3" data-halign="center" data-align="center" data-sortable="true">Last 3 Games</th>
   </tr>
 </thead>
</table>

<br><br>
<br><br>

### Positional Breakdown by Week

```echarts
{
    "grid": {
        "top": "10%",
        "bottom": "15%",
        "left": "20%",
        "right": "10%"
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
            "Pink Pony Club",
            "Hamlin My Business ",
            "Who Killed Charbonne",
            "Tom and Jerry",
            "To Infinity and Bija",
            "Hit and Ruggs",
            "Mama Daughter Duo",
            "Abbey Road to Victor",
            "Michael's Managable ",
            "Fantasy Guru Kayden"
        ],
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
```
