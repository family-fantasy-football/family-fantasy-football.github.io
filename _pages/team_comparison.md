---
layout: default
permalink: /comparison/
title: comparison
nav: false
nav_order: 3
description: 
chart:
    echarts: true
pretty_table: True
---
<script src="/assets/js/team-comparison.js"></script>
<div class="container mt-4">
  <div class="row">
    <!-- Team 1 Comparison -->
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          <h5>Team 1</h5>
        </div>
        <div class="card-body">
          <select id="team1-select" class="form-control mb-3">
            <option value="">Select Team</option>
          </select>
          <div id="team1-stats" class="mt-3">
            <!-- Team 1 stats will go here -->
          </div>
        </div>
      </div>
    </div>
    <!-- Team 2 Comparison -->
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          <h5>Team 2</h5>
        </div>
        <div class="card-body">
          <select id="team2-select" class="form-control mb-3">
            <option value="">Select Team</option>
          </select>
          <div id="team2-stats" class="mt-3">
            <!-- Team 2 stats will go here -->
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Button to Compare Teams -->
  <div class="row mt-3">
    <div class="col-12 text-center">
      <button id="compare-btn" class="btn btn-primary">Compare Teams</button>
    </div>
  </div>
  <!-- Comparison Results -->
  <div id="comparison-results" class="mt-4" style="display:none;">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div id="comparison-table-div">
          <!-- Comparison table will be inserted here -->
        </div>
      </div>
    </div>
  </div>
</div>
<br>
<!-- Chart container -->
<div id="chart-container" style="height: 400px; width: 100%;"></div>

<!-- Pie Charts Row -->
<div class="row mt-4">
  <div class="col-md-6">
    <div id="team1-pie" style="height: 300px; width: 100%;"></div>
  </div>
  <div class="col-md-6">
    <div id="team2-pie" style="height: 300px; width: 100%;"></div>
  </div>
</div>