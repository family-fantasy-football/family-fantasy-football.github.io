---
layout: page
permalink: /playoffs/simulator/
title: playoff simulator
nav: false
nav_order: 7
description: Simulate playoff scenarios
---
<style>
  table[data-toggle="table"] tbody td {{
    color: #2c3e50 !important;
  }}
</style>

<style>
.simulator-container {
    max-width: 1400px;
    margin: 0 auto;
}

.controls {
    display: flex;
    gap: 10px;
    margin: 20px 0;
    padding: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 10px;
    justify-content: center;
    flex-wrap: wrap;
}

.btn-sim {
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 15px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.btn-sim:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
}

.btn-secondary { background: #34495e; color: white; }
.btn-secondary { background: #34495e; color: white; }
.btn-success { background: #27ae60; color: white; }

.week-section {
    margin: 30px 0;
}

.week-header {
    font-size: 24px;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 3px solid #3498db;
}

.game-card {
    background: white;
    border-radius: 12px;
    padding: 20px;
    margin: 20px 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.07);
    transition: all 0.3s ease;
}

.game-card:hover {
    box-shadow: 0 8px 15px rgba(0,0,0,0.1);
}

.matchup-container {
    display: flex;
    gap: 20px;
    align-items: stretch;
}

.team-card {
    flex: 1;
    padding: 20px;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 3px solid #e0e0e0;
    background: #f8f9fa;
    text-align: center;
    position: relative;
}

.team-card:hover {
    transform: scale(1.02);
    border-color: #3498db;
}

.team-card.selected {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-color: #667eea;
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.team-name {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 15px;
}

.location-badge {
    position: absolute;
    top: 10px;
    right: 10px;
    background: #e74c3c;
    color: white;
    padding: 4px 8px;
    border-radius: 5px;
    font-size: 11px;
    font-weight: bold;
}

.team-card.selected .location-badge {
    background: #f39c12;
}

.score-section {
    margin-top: 15px;
    padding-top: 15px;
    border-top: 2px solid rgba(0,0,0,0.1);
}

.team-card.selected .score-section {
    border-top-color: rgba(255,255,255,0.3);
}

.score-label {
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #7f8c8d;
}

.team-card.selected .score-label {
    color: rgba(255,255,255,0.9);
}

.score-input {
    width: 100%;
    max-width: 120px;
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 6px;
    font-size: 16px;
    text-align: center;
    transition: all 0.3s ease;
    font-weight: bold;
}

.score-input:focus {
    outline: none;
    border-color: #3498db;
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

.team-card.selected .score-input {
    background: white;
    border-color: white;
}

.vs-divider {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: bold;
    color: #95a5a6;
    min-width: 40px;
}

.standings-section {
    margin: 50px 0;
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.07);
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 25px;
}

.standings-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
}

.standings-table thead {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.standings-table th {
    padding: 15px;
    text-align: left;
    font-weight: 600;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.standings-table th:first-child {
    border-top-left-radius: 8px;
}

.standings-table th:last-child {
    border-top-right-radius: 8px;
}

.standings-table td {
    padding: 15px;
    border-bottom: 1px solid #ecf0f1;
}

.standings-table tbody tr {
    transition: all 0.2s ease;
}

.standings-table tbody tr:hover {
    background: #f8f9fa;
}

.standings-table tbody tr:last-child td {
    border-bottom: none;
}

.in-playoffs {
    background: #d5f4e6 !important;
    border-left: 4px solid #27ae60;
}

.on-bye {
    background: #fff9e6 !important;
    border-left: 4px solid #f39c12;
}

.status-badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: bold;
}

.status-bye {
    background: #f39c12;
    color: white;
}

.status-playoff {
    background: #27ae60;
    color: white;
}

.status-out {
    background: #e74c3c;
    color: white;
}

.bracket-section {
    margin: 50px 0;
    padding: 30px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.07);
}

.bracket {
    display: flex;
    justify-content: space-around;
    margin: 30px 0;
    flex-wrap: nowrap;
    overflow-x: auto;
    padding: 20px;
}

.bracket-round {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    min-width: 280px;
    margin: 0 15px;
}

.round-title {
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
    padding: 12px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 8px;
}

.bracket-game {
    border: 3px solid #34495e;
    border-radius: 10px;
    padding: 15px;
    margin: 15px 0;
    background: white;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.bracket-team {
    padding: 12px 15px;
    margin: 5px 0;
    background: #f8f9fa;
    border-radius: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 500;
    transition: all 0.3s ease;
}

.bracket-team.winner {
    background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);
    color: white;
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(86, 171, 47, 0.3);
}

.bracket-team.loser {
    background: #e8e8e8;
    opacity: 0.5;
}

.seed-badge {
    background: #34495e;
    color: white;
    border-radius: 50%;
    width: 28px;
    height: 28px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    font-weight: bold;
    margin-right: 10px;
}

.bye-indicator {
    background: linear-gradient(135deg, #f39c12 0%, #f1c40f 100%);
    color: white;
    padding: 15px;
    border-radius: 8px;
    text-align: center;
    font-weight: bold;
    font-size: 16px;
}

@media (max-width: 768px) {
    .matchup-container {
        flex-direction: column;
    }
    
    .vs-divider {
        transform: rotate(90deg);
        margin: 10px 0;
    }
    
    .bracket {
        flex-direction: column;
    }
    
    .bracket-round {
        min-width: 100%;
        margin: 20px 0;
    }
}
.magic-numbers-section {
    margin: 30px 0;
    padding: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 12px;
    color: white;
}

.magic-table {
    width: 100%;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    margin-top: 15px;
    color: #2c3e50;
}

.magic-table th {
    background: #34495e;
    color: white;
    padding: 12px;
    text-align: left;
}

.magic-table td {
    padding: 12px;
    border-bottom: 1px solid #ecf0f1;
}

.status-clinched { color: #27ae60; font-weight: bold; }
.status-eliminated { color: #e74c3c; font-weight: bold; }
.status-active { color: #f39c12; font-weight: bold; }

.scenarios-section {
    margin: 30px 0;
}

.scenario-card {
    background: white;
    border-radius: 10px;
    padding: 20px;
    margin: 15px 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.scenario-card h4 {
    margin: 0 0 10px 0;
    color: #2c3e50;
}

.scenario-item {
    padding: 8px 0;
    border-left: 3px solid #3498db;
    padding-left: 15px;
    margin: 8px 0;
}
</style>

<div class="simulator-container" id="playoff-simulator">
    

    <div class="controls">
        <button class="btn-sim btn-primary" onclick="resetSimulator()">🔄 Reset All</button>
        <button class="btn-sim btn-secondary" onclick="simulateAllGames('random')">🎲 Simulate Random</button>
        <button class="btn-sim btn-success" onclick="simulateAllGames('favorite')">⭐ Pick All Favorites</button>
    </div>

    <div id="game-selections"></div>

    <div class="standings-section" id="current-standings">
        <h2 class="section-title">📊 Projected Final Standings</h2>
        <table class="standings-table">
            <thead>
                <tr>
                    <th>Seed</th>
                    <th>Team</th>
                    <th>Record</th>
                    <th>Points For</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody id="standings-body"></tbody>
        </table>
    </div>

    <div class="bracket-section" id="playoff-bracket">
        <h2 class="section-title">🏆 Playoff Bracket</h2>
        <div id="bracket-container"></div>
    </div>
</div>

<script src="{{ '/assets/js/playoff_simulator.js' | relative_url }}"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        fetch('{{ "/assets/json/playoffs/simulator_data.json" | relative_url }}')
            .then(response => response.json())
            .then(data => {
                window.simulatorData = data;
                initializeSimulator(data);
                loadMagicNumbers(data.magic_numbers);
                loadScenarios(data.scenarios);
            });
    });
    
    function loadMagicNumbers(magicNumbers) {
        const tbody = document.getElementById('magic-numbers-body');
        tbody.innerHTML = '';
        
        magicNumbers.forEach(item => {
            const row = document.createElement('tr');
            const statusClass = `status-${item.status.toLowerCase()}`;
            
            row.innerHTML = `
                <td>${item.rank}</td>
                <td><strong>${item.team}</strong></td>
                <td>${item.current_record}</td>
                <td>${item.remaining_games}</td>
                <td>${item.clinch_number || '-'}</td>
                <td>${item.elimination_number || '-'}</td>
                <td class="${statusClass}">${item.status}</td>
            `;
            tbody.appendChild(row);
        });
    }
    
    function loadScenarios(scenarios) {
        const container = document.getElementById('scenarios-container');
        container.innerHTML = '';
        
        scenarios.forEach(item => {
            const card = document.createElement('div');
            card.className = 'scenario-card';
            
            let html = `<h4>${item.rank}. ${item.team}</h4>`;
            
            item.scenarios.forEach(scenario => {
                html += `<div class="scenario-item">${scenario}</div>`;
            });
            
            if (item.remaining_opponents.length > 0) {
                html += `<div style="margin-top: 10px; font-size: 0.9em; color: #7f8c8d;">
                    <strong>Remaining opponents:</strong> ${item.remaining_opponents.join(', ')}
                </div>`;
            }
            
            card.innerHTML = html;
            container.appendChild(card);
        });
    }
</script>
