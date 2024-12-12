document.addEventListener('DOMContentLoaded', function() {
    // Load team and player data
    fetch('/assets/json/trade_analyzer/players_2024.json')
        .then(response => response.json())
        .then(data => initializeTradeAnalyzer(data));
});

function initializeTradeAnalyzer(playerData) {
    const teams = [...new Set(playerData.map(p => p.team))];
    populateTeamSelects(teams);

    // Event listeners for team selection
    document.getElementById('team1-select').addEventListener('change', function() {
        populatePlayerSelect('team1-players', this.value, playerData);
    });

    document.getElementById('team2-select').addEventListener('change', function() {
        populatePlayerSelect('team2-players', this.value, playerData);
    });

    // Analyze button click handler
    document.getElementById('analyze-btn').addEventListener('click', function() {
        analyzeTrade(playerData);
    });
}

function populateTeamSelects(teams) {
    const selects = ['team1-select', 'team2-select'];
    teams.sort();
    
    selects.forEach(selectId => {
        const select = document.getElementById(selectId);
        select.innerHTML = '<option value="">Select Team</option>';
        teams.forEach(team => {
            select.innerHTML += `<option value="${team}">${team}</option>`;
        });
    });
}

function populatePlayerSelect(selectId, team, playerData) {
    const select = document.getElementById(selectId);
    select.innerHTML = '';
    const teamPlayers = playerData.filter(p => p.team === team);
    
    // Group by position and sort by projected points
    const positions = ['QB', 'RB', 'WR', 'TE', 'K', 'D/ST'];
    positions.forEach(pos => {
        const posPlayers = teamPlayers
            .filter(p => p.position === pos)
            .sort((a, b) => b.ros_projection - a.ros_projection);
            
        if (posPlayers.length > 0) {
            const optgroup = document.createElement('optgroup');
            optgroup.label = pos;
            posPlayers.forEach(player => {
                const option = document.createElement('option');
                option.value = player.id;
                option.text = `${player.name} (${player.avg_points} pts/g)`;
                optgroup.appendChild(option);
            });
            select.appendChild(optgroup);
        }
    });
}

function analyzeTrade(playerData) {
    const team1Players = getSelectedPlayers('team1-players', playerData);
    const team2Players = getSelectedPlayers('team2-players', playerData);
    
    if (team1Players.length === 0 || team2Players.length === 0) {
        alert('Please select players from both teams');
        return;
    }

    const analysis = {
        team1: analyzeTradeImpact(team1Players, team2Players),
        team2: analyzeTradeImpact(team2Players, team1Players)
    };

    displayAnalysis(analysis);
    createTradeChart(team1Players, team2Players);
    document.getElementById('analysis-results').style.display = 'block';
}

function analyzeTradeImpact(givingPlayers, receivingPlayers) {
    const pointsGiving = givingPlayers.reduce((sum, p) => sum + p.ros_projection, 0);
    const pointsReceiving = receivingPlayers.reduce((sum, p) => sum + p.ros_projection, 0);
    const netChange = pointsReceiving - pointsGiving;
    
    return {
        pointsGiving,
        pointsReceiving,
        netChange,
        positionImpact: analyzePositionImpact(givingPlayers, receivingPlayers)
    };
}

function analyzePositionImpact(givingPlayers, receivingPlayers) {
    const positions = ['QB', 'RB', 'WR', 'TE', 'K', 'D/ST'];
    const impact = {};
    
    positions.forEach(pos => {
        const giving = givingPlayers.filter(p => p.position === pos);
        const receiving = receivingPlayers.filter(p => p.position === pos);
        if (giving.length > 0 || receiving.length > 0) {
            impact[pos] = {
                giving: giving.reduce((sum, p) => sum + p.ros_projection, 0),
                receiving: receiving.reduce((sum, p) => sum + p.ros_projection, 0)
            };
        }
    });
    
    return impact;
}

function displayAnalysis(analysis) {
    ['team1', 'team2'].forEach(team => {
        const analysisDiv = document.getElementById(`${team}-analysis`);
        const data = analysis[team];
        
        let html = `
            <div class="card-body">
                <h5>Projected ROS Impact</h5>
                <p>Giving up: ${data.pointsGiving.toFixed(1)} points</p>
                <p>Receiving: ${data.pointsReceiving.toFixed(1)} points</p>
                <p class="font-weight-bold ${data.netChange > 0 ? 'text-success' : 'text-danger'}">
                    Net change: ${data.netChange.toFixed(1)} points
                </p>
                <h6>Position Impact:</h6>
                <ul>
        `;
        
        Object.entries(data.positionImpact).forEach(([pos, impact]) => {
            const netPosChange = impact.receiving - impact.giving;
            html += `
                <li>${pos}: ${netPosChange > 0 ? '+' : ''}${netPosChange.toFixed(1)} points</li>
            `;
        });
        
        html += '</ul></div>';
        analysisDiv.innerHTML = html;
    });
}

function createTradeChart(team1Players, team2Players) {
    const team1Name = document.getElementById('team1-select').value;
    const team2Name = document.getElementById('team2-select').value;
    
    const option = {
        title: {
            text: 'Trade Comparison',
            left: 'center'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['Points Giving', 'Points Receiving'],
            top: 25
        },
        xAxis: {
            type: 'category',
            data: [team1Name, team2Name]
        },
        yAxis: {
            type: 'value',
            name: 'Projected ROS Points'
        },
        series: [
            {
                name: 'Points Giving',
                type: 'bar',
                data: [
                    team1Players.reduce((sum, p) => sum + p.ros_projection, 0),
                    team2Players.reduce((sum, p) => sum + p.ros_projection, 0)
                ]
            },
            {
                name: 'Points Receiving',
                type: 'bar',
                data: [
                    team2Players.reduce((sum, p) => sum + p.ros_projection, 0),
                    team1Players.reduce((sum, p) => sum + p.ros_projection, 0)
                ]
            }
        ]
    };

    echarts.init(document.getElementById('trade-chart')).setOption(option);
}

function getSelectedPlayers(selectId, playerData) {
    const select = document.getElementById(selectId);
    const selectedValues = Array.from(select.selectedOptions).map(opt => opt.value);
    return playerData.filter(p => selectedValues.includes(p.id.toString()));
}