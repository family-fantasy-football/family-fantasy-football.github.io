---
layout: page
title: teams
permalink: /teams/
description:
nav: true
nav_order: 1
display_categories: 2025-26
horizontal: false
dropdown: true
children:
    - title: 90s
      permalink: /teams/90s_2025/
    - title: divider
    - title: ARV
      permalink: /teams/ARV_2025/
    - title: divider
    - title: BTE
      permalink: /teams/BTE_2025/
    - title: divider
    - title: EET
      permalink: /teams/EET_2025/
    - title: divider
    - title: HMB
      permalink: /teams/HMB_2025/
    - title: divider
    - title: JST
      permalink: /teams/JST_2025/
    - title: divider
    - title: KTT
      permalink: /teams/KTT_2025/
    - title: divider
    - title: MMT
      permalink: /teams/MMT_2025/
    - title: divider
    - title: RRT
      permalink: /teams/RRT_2025/
    - title: divider
    - title: TIB
      permalink: /teams/TIB_2025/
    - title: divider
    - title: TOM
      permalink: /teams/TOM_2025/
    - title: divider
    - title: TTC
      permalink: /teams/TTC_2025/
---

<!-- pages/teams.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
    </div>
  </div>
  {% endif %}
  {% endfor %}

{% else %}

  <!-- Display projects without categories -->
  {% assign sorted_projects = site.projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
    </div>
  </div>
  {% endif %}
{% endif %}
