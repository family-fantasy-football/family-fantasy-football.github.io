---
layout: page
permalink: /players/compare/
title: player comparison
nav: false
nav_order: 3
custom_js:
    - player-comparison
description: Compare player performance and projections
chart:
    echarts: true
pretty_table: True
---
<style>
  table[data-toggle="table"] tbody td {
    color: #2c3e50 !important;
  }
</style>
<script src="/assets/js/player-comparison.js"></script>
<div class="container mt-4">
    <div class="row">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>Player 1</h5>
                </div>
                <div class="card-body">
                    <select id="player1-select" class="form-control mb-3">
                        <option value="">Select Player</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>Player 2</h5>
                </div>
                <div class="card-body">
                    <select id="player2-select" class="form-control mb-3">
                        <option value="">Select Player</option>
                    </select>
                </div>
            </div>
        </div>
    </div>
    
    <div class="row mt-3">
        <div class="col-12 text-center">
            <button id="compare-btn" class="btn btn-primary">Compare Players</button>
        </div>
    </div>

    <div id="comparison-results" class="mt-4" style="display:none;">
        <div class="row">
            <div class="col-12">
                <div id="weekly-chart" style="height: 400px; width: 100%; position: relative;"></div>
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-md-6">
                <div id="player1-stats" class="card">
                </div>
            </div>
            <div class="col-md-6">
                <div id="player2-stats" class="card">
                </div>
            </div>
        </div>
    </div>
</div>