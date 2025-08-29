document.addEventListener('DOMContentLoaded', function() {
    let playerData = [];
    const darkMode = document.body.classList.contains('dark');
    let echartsTheme = document.body.classList.contains('dark');
    // Load player data
    fetch('/assets/json/player_comparison/players_2025.json')
        .then(response => response.json())
        .then(data => {
            playerData = data;
            populatePlayerSelects(data);
        });

    function populatePlayerSelects(data) {
        const selects = ['#player1-select', '#player2-select'];
        selects.forEach(select => {
            const selectEl = document.querySelector(select);
            selectEl.innerHTML = '<option value="">Select Player</option>';
            
            // Group players by position
            const positions = ['QB', 'RB', 'WR', 'TE'];
            positions.forEach(pos => {
                const posPlayers = data.filter(p => p.position === pos);
                if (posPlayers.length) {
                    const optgroup = document.createElement('optgroup');
                    optgroup.label = pos;
                    posPlayers.sort((a, b) => b.total_points - a.total_points)
                        .forEach(player => {
                            const option = document.createElement('option');
                            option.value = player.id;
                            option.textContent = `${player.name} (${player.team})`;
                            optgroup.appendChild(option);
                        });
                    selectEl.appendChild(optgroup);
                }
            });
        });
    }

    document.querySelector('#compare-btn').addEventListener('click', function() {
        const player1Id = document.querySelector('#player1-select').value;
        const player2Id = document.querySelector('#player2-select').value;
        
        if (!player1Id || !player2Id) {
            alert('Please select two players to compare');
            return;
        }
        
        const player1 = playerData.find(p => p.id === parseInt(player1Id));
        const player2 = playerData.find(p => p.id === parseInt(player2Id));
        
        createWeeklyChart(player1, player2);
        displayPlayerStats(player1, player2);
        document.querySelector('#comparison-results').style.display = 'block';
    });

    function createWeeklyChart(player1, player2) {
        const chartDiv = document.getElementById('weekly-chart');
        // const chart = echarts.init(chartDiv);
        const weeks = player1.weekly_points.map((_, i) => `Week ${i + 1}`);
        if (echartsTheme === 'dark') {
            var chart = echarts.init(chartDiv, 'dark-fresh-cut');
          } else {
            var chart = echarts.init(chartDiv);
          }
        const option = {
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data: [player1.name, player2.name]
            },
            xAxis: {
                type: 'category',
                data: weeks
            },
            yAxis: {
                type: 'value',
                name: 'Points'
            },
            series: [
                {
                    name: player1.name,
                    type: 'line',
                    data: player1.weekly_points,
                    smooth: true
                },
                {
                    name: player2.name,
                    type: 'line',
                    data: player2.weekly_points,
                    smooth: true
                }
            ]
        };
        
        chart.setOption(option);
        window.addEventListener('resize', () => chart.resize());

// Also resize immediately after setting options
        setTimeout(() => chart.resize(), 0);
    }   

    function displayPlayerStats(player1, player2) {
        const statGroups = {
            'Basic Stats': {
                points_per_game: 'Points/Game',
                total_points: 'Total Points',
                games_played: 'Games Played',
                projected_points: 'Projected Points'
            },
            'Consistency Metrics': {
                std_dev: 'Std Deviation',
                floor: 'Floor',
                ceiling: 'Ceiling',
                consistency: 'Consistency %'
            },
            'Position Context': {
                team_share: 'League Team Points Share %',
                pos_avg_diff: 'vs Position NFL Starter Avg'
            },
            'League Context': {
                percent_owned: 'Roster %',
                percent_started: 'Started %'
            }
        };
    
        ['player1-stats', 'player2-stats'].forEach((elementId, index) => {
            const player = index === 0 ? player1 : player2;
            let html = `
                <div class="card-body">
                    <h5 class="card-title">${player.name} (${player.position})</h5>
                    <p class="card-text">Team: ${player.team}</p>
            `;
            
            // Add each stat group
            Object.entries(statGroups).forEach(([groupName, stats]) => {
                html += `
                    <div class="stat-group mb-3">
                        <h6 class="border-bottom pb-2 mb-2">${groupName}</h6>
                        ${Object.entries(stats).map(([stat, label]) => `
                            <div class="row mb-1 ${stat === 'pos_avg_diff' && player[stat] > 0 ? 'text-success' : 
                                                 stat === 'pos_avg_diff' && player[stat] < 0 ? 'text-danger' : ''}">
                                <div class="col-7">${label}:</div>
                                <div class="col-5 text-end">${
                                    typeof player[stat] === 'number' ? 
                                    (stat.includes('percent') || stat.includes('consistency') || stat.includes('share') ? 
                                        player[stat].toFixed(1) + '%' : 
                                        player[stat].toFixed(1)) : 
                                    player[stat] || 'N/A'
                                }</div>
                            </div>
                        `).join('')}
                    </div>
                `;
            });
            
            html += '</div>';
            document.getElementById(elementId).innerHTML = html;
        });
    }
});