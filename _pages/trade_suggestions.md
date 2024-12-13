---
layout: page
permalink: /trades/trade_suggestions/
title: trade suggestions
nav: false
nav_order: 7
custom_js:
    - trade-suggestions
description: Get personalized trade suggestions based on team needs
chart:
    echarts: true
pretty_table: True
---
<script src="/assets/js/trade-suggestions.js"></script>

This only displays trades that have a net benefit to both trade partners. I think that is is working correctly. 

<center>
<div class="container mt-4">
    <div class="row d-flex justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h5>Your Team</h5>
                </div>
                <div class="card-body">
                    <select id="team-select" class="form-control mb-3">
                        <option value="">Select Your Team</option>
                    </select>
                    <div class="mb-3">
                        <label class="form-label">Position Focus (Optional)</label>
                        <select id="position-select" class="form-control">
                            <option value="">All Positions</option>
                            <option value="QB">QB</option>
                            <option value="RB">RB</option>
                            <option value="WR">WR</option>
                            <option value="TE">TE</option>
                        </select>
                    </div>
                    <div class="mb-3">
    <label class="form-label">Trade Partner (Optional)</label>
    <select id="partner-select" class="form-control">
        <option value="">Any Team</option>
    </select>
</div>

<div class="mb-3">
    <label class="form-label">Target Specific Player</label>
    <input type="text" id="target-player" class="form-control" placeholder="Search for player...">
    <select id="target-player-select" class="form-control mt-2" style="display:none;">
    </select>
</div>
                    <div class="mb-3">
                        <label class="form-label">Untouchable Players</label>
                        <select id="locked-players" class="form-control" multiple size="6">
                        </select>
                    </div>
                    <div class="mb-3">
    <label class="form-label">Maximum Players to Trade</label>
    <select id="max-players" class="form-control">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>
</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="row mt-3">
        <div class="col-12 text-center">
            <button id="suggest-btn" class="btn btn-primary">Get Suggestions</button>
        </div>
    </div>

    <div id="suggestions-results" class="mt-4" style="display:none;">
        <!-- Results will be populated by JavaScript -->
    </div>
</div>
</center>