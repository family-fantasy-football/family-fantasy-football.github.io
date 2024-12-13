---
layout: page
permalink: /trades/trade_analyzer/
title: trade analyzer
nav: false
nav_order: 6
custom_js:
    - trade-analyzer
description: Analyze potential trades using projections and historical data
chart:
    echarts: true
pretty_table: True
---
<script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
<script src="../../assets/js/trade-analyzer.js"></script>

<div class="container mt-4">
...

<div class="container mt-4">
    <div class="row">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>Team 1</h5>
                </div>
                <div class="card-body">
                    <select id="team1-select" class="form-control mb-3">
                        <option value="">Select Team</option>
                    </select>
                    <select id="team1-players" class="form-control" multiple size="8">
                    </select>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>Team 2</h5>
                </div>
                <div class="card-body">
                    <select id="team2-select" class="form-control mb-3">
                        <option value="">Select Team</option>
                    </select>
                    <select id="team2-players" class="form-control" multiple size="8">
                    </select>
                </div>
            </div>
        </div>
    </div>
    
    <div class="row mt-3">
        <div class="col-12 text-center">
            <button id="analyze-btn" class="btn btn-primary">Analyze Trade</button>
        </div>
    </div>

    <div id="analysis-results" class="mt-4" style="display:none;">
        <div class="row">
            <div class="col-md-6">
                <div id="team1-analysis" class="card">
                </div>
            </div>
            <div class="col-md-6">
                <div id="team2-analysis" class="card">
                </div>
            </div>
        </div>
        <div class="row mt-3">
            <div class="col-12">
                <div id="trade-chart"></div>
            </div>
        </div>
    </div>
</div>
