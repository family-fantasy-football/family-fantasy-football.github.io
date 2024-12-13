document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const teamSelect = document.getElementById('team-select');
    const positionSelect = document.getElementById('position-select');
    const partnerSelect = document.getElementById('partner-select');
    const lockedPlayers = document.getElementById('locked-players');
    const targetPlayerInput = document.getElementById('target-player');
    const targetPlayerSelect = document.getElementById('target-player-select');
    const maxPlayers = document.getElementById('max-players');
    const suggestBtn = document.getElementById('suggest-btn');
    const resultsDiv = document.getElementById('suggestions-results');

    // Store all rosters and player data
    let allRosters = {};
    let allPlayers = {};
    let teamAbbrevs = {};

    // Load teams and roster data at startup
    Promise.all([
        fetch('../../assets/json/standings.json'),
        fetch('../../assets/json/player_comparison/players_2024.json')
    ])
    .then(([standingsResponse, playersResponse]) => 
        Promise.all([standingsResponse.json(), playersResponse.json()]))
    .then(([standings, players]) => {
        // Store player data
        allPlayers = players;
        
        // Populate team selects
        standings.forEach(team => {
            [teamSelect, partnerSelect].forEach(select => {
                const option = document.createElement('option');
                option.value = team.team;
                option.textContent = team.team;
                select.appendChild(option);
            });
            teamAbbrevs[team.team] = team.abbrev;
        });

        // Load rosters
        const rosterPromises = standings.map(team => 
            fetch(`../../assets/json/team_rosters/${team.abbrev}_2024.json`)
                .then(response => response.json())
                .then(roster => {
                    allRosters[team.team] = roster;
                })
        );

        return Promise.all(rosterPromises);
    })
    .catch(error => console.error('Error loading data:', error));

    // Update locked players when team is selected
    teamSelect.addEventListener('change', function() {
        lockedPlayers.innerHTML = '';
        const roster = (allRosters[this.value] || [])
        .filter(player => player.injury_stat !== 'INJURY_RESERVE');
        roster.forEach(player => {
            const option = document.createElement('option');
            option.value = player.player_name;
            option.textContent = `${player.player_name} (${player.pos}) - ${player.avg_points} PPG`;
            lockedPlayers.appendChild(option);
        });
    });

    // Handle player search
    targetPlayerInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        if (searchTerm.length < 2) {
            targetPlayerSelect.style.display = 'none';
            return;
        }

        targetPlayerSelect.innerHTML = '';
        targetPlayerSelect.style.display = 'block';

        Object.values(allPlayers)
            .filter(player => 
                player.name.toLowerCase().includes(searchTerm))
            .slice(0, 10)  // Limit to top 10 matches
            .forEach(player => {
                const option = document.createElement('option');
                option.value = player.name;
                option.textContent = `${player.name} (${player.position}) - ${player.avg_points} PPG`;
                targetPlayerSelect.appendChild(option);
            });
    });

    function validatePositionalRequirements(team, playersToTrade, playersToReceive) {
        const posLimits = { QB: 2, RB: 3, WR: 3, TE: 1 };
        const roster = allRosters[team];
        
        // Count current players by position
        const posCounts = {};
        roster.forEach(player => {
            posCounts[player.pos] = (posCounts[player.pos] || 0) + 1;
        });

        // Adjust counts based on trade
        playersToTrade.forEach(player => {
            posCounts[player.pos]--;
        });
        
        playersToReceive.forEach(player => {
            posCounts[player.pos] = (posCounts[player.pos] || 0) + 1;
        });

        // Check if any position falls below minimum
        for (const [pos, limit] of Object.entries(posLimits)) {
            if ((posCounts[pos] || 0) < limit) {
                return false;
            }
        }
        
        return true;
    }

    function getTopPlayers(roster, position) {
        const posLimits = { QB: 2, RB: 3, WR: 3, TE: 1 };
        return roster
            .filter(p => p.pos === position)
            .sort((a, b) => parseFloat(b.avg_points) - parseFloat(a.avg_points))
            .slice(0, posLimits[position]);
    }

    function isQualityTrade(team, playersToTrade) {
        let topPlayerCount = 0;
        const roster = allRosters[team];

        playersToTrade.forEach(player => {
            const topPlayersAtPos = getTopPlayers(roster, player.pos);
            if (topPlayersAtPos.some(p => p.player_name === player.player_name)) {
                topPlayerCount++;
            }
        });

        return topPlayerCount >= Math.ceil(playersToTrade.length / 2);
    }

    function generateSuggestions(teamName, partnerTeam, targetPlayer, positionFocus, lockedPlayerSet) {
        const suggestions = [];
        const myRoster = allRosters[teamName];
        const maxTradeSize = parseInt(maxPlayers.value);

        // Get available teams to trade with
        const tradePartners = partnerTeam ? [partnerTeam] : 
            Object.keys(allRosters).filter(team => team !== teamName);

        tradePartners.forEach(partner => {
            const theirRoster = allRosters[partner];
            
            // Generate all valid trade combinations
            for (let size = 1; size <= maxTradeSize; size++) {
                const myValidCombos = generateCombinations(myRoster, size, lockedPlayerSet);
                const theirValidCombos = generateCombinations(theirRoster, size, new Set());

                myValidCombos.forEach(myCombination => {
                    if (!isQualityTrade(teamName, myCombination)) return;

                    theirValidCombos.forEach(theirCombination => {
                        if (!isQualityTrade(partner, theirCombination)) return;

                        // Validate positional requirements for both teams
                        if (!validatePositionalRequirements(teamName, myCombination, theirCombination) ||
                            !validatePositionalRequirements(partner, theirCombination, myCombination)) {
                            return;
                        }

                        // Calculate trade value
                        const myValue = myCombination.reduce((sum, p) => sum + parseFloat(p.avg_points), 0);
                        const theirValue = theirCombination.reduce((sum, p) => sum + parseFloat(p.avg_points), 0);
                        const myImpact = calculateTradeImpact(teamName, myCombination, theirCombination);
                        const theirImpact = calculateTradeImpact(partner, theirCombination, myCombination);
                        const valueDiff = myValue - theirValue;
                        if (valueDiff <= 5 && 
                            myImpact.totalImprovement > 0 && 
                            theirImpact.totalImprovement > 0) {
                            suggestions.push({
                                partnerTeam: partner,
                                giving: myCombination,
                                receiving: theirCombination,
                                myValue: myValue,
                                theirValue: theirValue,
                                myImpact: myImpact,
                                theirImpact: theirImpact,
                                netValue: (myImpact.totalImprovement + theirImpact.totalImprovement) / 2
                            });
                        }
                        // Only suggest relatively fair trades
                        // if (valueDiff <= 5) {
                        //     suggestions.push({
                        //         partnerTeam: partner,
                        //         giving: myCombination,
                        //         receiving: theirCombination,
                        //         myValue: myValue,
                        //         theirValue: theirValue,
                        //         netValue: theirValue - myValue
                        //     });
                        // }
                    });
                });
            }
        });
        const sortedSuggestions = suggestions.sort((a, b) => b.myImpact.totalImprovement - a.myImpact.totalImprovement);
        // Sort by trade value and fairness
        const partnerCounts = {};
        return sortedSuggestions.filter(sugg => {
            partnerCounts[sugg.partnerTeam] = (partnerCounts[sugg.partnerTeam] || 0) + 1;
            return partnerCounts[sugg.partnerTeam] <= 2;
        }).slice(0, 5);
            }

    function generateCombinations(roster, size, excludedPlayers) {
        const available = roster.filter(p => 
            !excludedPlayers.has(p.player_name) && 
            p.injury_stat !== 'INJURY_RESERVE'
        );
        console.log(available)
        const combinations = [];

        function combine(start, combo) {
            if (combo.length === size) {
                combinations.push([...combo]);
                return;
            }
            
            for (let i = start; i < available.length; i++) {
                combo.push(available[i]);
                combine(i + 1, combo);
                combo.pop();
            }
        }

        combine(0, []);
        return combinations;
    }

    function calculateTradeImpact(team, playersLosing, playersGaining) {
        const roster = allRosters[team];
        const positionGroups = { QB: [], RB: [], WR: [], TE: [] };
        
        // Group current roster by position
        roster.forEach(player => {
            if (positionGroups[player.pos]) {
                positionGroups[player.pos].push({
                    name: player.player_name,
                    ppg: parseFloat(player.avg_points)
                });
            }
        });
        
        // Calculate current positional strength
        const currentStrength = calculatePositionalStrength(positionGroups);
        
        // Remove players being traded away
        playersLosing.forEach(player => {
            if (positionGroups[player.pos]) {
                positionGroups[player.pos] = positionGroups[player.pos]
                    .filter(p => p.name !== player.player_name);
            }
        });
        
        // Add players being received
        playersGaining.forEach(player => {
            if (positionGroups[player.pos]) {
                positionGroups[player.pos].push({
                    name: player.player_name,
                    ppg: parseFloat(player.avg_points)
                });
            }
        });
        
        // Calculate new strength
        const newStrength = calculatePositionalStrength(positionGroups);
        
        // Calculate improvements by position
        const improvements = {};
        let totalImprovement = 0;
        
        Object.keys(positionGroups).forEach(pos => {
            improvements[pos] = newStrength[pos] - currentStrength[pos];
            totalImprovement += improvements[pos];
        });
        
        return {
            improvements,
            totalImprovement,
            currentStrength,
            newStrength
        };
    }
    
    function calculatePositionalStrength(positionGroups) {
        const posLimits = { QB: 2, RB: 3, WR: 3, TE: 1 };
        const strength = {};
        
        Object.entries(positionGroups).forEach(([pos, players]) => {
            const sortedPlayers = players.sort((a, b) => b.ppg - a.ppg);
            const limit = posLimits[pos];
            const topPlayers = sortedPlayers.slice(0, limit);
            strength[pos] = topPlayers.reduce((sum, p) => sum + p.ppg, 0) / Math.max(1, topPlayers.length);
        });
        
        return strength;
    }

    suggestBtn.addEventListener('click', function() {
        const selectedTeam = teamSelect.value;
        const selectedPartner = partnerSelect.value;
        const targetPlayerName = targetPlayerInput.value;
        const positionFocus = positionSelect.value;
        const lockedPlayerSet = new Set(
            Array.from(lockedPlayers.selectedOptions).map(opt => opt.value)
        );

        if (!selectedTeam) {
            alert('Please select your team');
            return;
        }

        const suggestions = generateSuggestions(
            selectedTeam,
            selectedPartner,
            targetPlayerName,
            positionFocus,
            lockedPlayerSet
        );

        displaySuggestions(suggestions);
    });

    function displaySuggestions(suggestions) {
        resultsDiv.style.display = 'block';
        resultsDiv.innerHTML = '';
    
        function displayPositionalImpact(impact) {
            return Object.entries(impact.improvements)
                .map(([pos, value]) => {
                    const color = value > 0 ? 'text-success' : value < 0 ? 'text-danger' : 'text-muted';
                    return `<li>${pos}: <span class="${color}">${value > 0 ? '+' : ''}${value.toFixed(2)} PPG</span></li>`;
                })
                .join('');
        }
    
        if (suggestions.length === 0) {
            resultsDiv.innerHTML = '<div class="alert alert-info">No valid trade suggestions found.</div>';
            return;
        }
    
        suggestions.forEach(suggestion => {
            const card = document.createElement('div');
            card.className = 'card mb-3';
            card.innerHTML = `
                <div class="card-header">
                    <h5>Trade with ${suggestion.partnerTeam}</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-6">
                            <h6>You Give:</h6>
                            <ul class="list-unstyled">
                                ${suggestion.giving.map(p => 
                                    `<li>${p.player_name} (${p.pos}) - ${p.avg_points} PPG</li>`
                                ).join('')}
                            </ul>
                            <h6>${teamAbbrevs[teamSelect.value]} Position Group Changes:</h6>
                            <ul class="list-unstyled">
                                ${displayPositionalImpact(suggestion.myImpact)}
                            </ul>
                            <p><strong>Total Impact: ${suggestion.myImpact.totalImprovement.toFixed(2)} PPG</strong></p>
                        </div>
                        <div class="col-md-6">
                            <h6>You Receive:</h6>
                            <ul class="list-unstyled">
                                ${suggestion.receiving.map(p => 
                                    `<li>${p.player_name} (${p.pos}) - ${p.avg_points} PPG</li>`
                                ).join('')}
                            </ul>
                            <h6>${teamAbbrevs[suggestion.partnerTeam]} Position Group Changes:</h6>
                            <ul class="list-unstyled">
                                ${displayPositionalImpact(suggestion.theirImpact)}
                            </ul>
                            <p><strong>Total Impact: ${suggestion.theirImpact.totalImprovement.toFixed(2)} PPG</strong></p>
                        </div>
                    </div>
                    <div class="text-center mt-2">
                        <p class="mb-0">
                            <strong>Net Value: ${suggestion.netValue > 0 ? '+' : ''}${suggestion.netValue.toFixed(2)} PPG</strong>
                        </p>
                    </div>
                </div>
            `;
            resultsDiv.appendChild(card);
        });
    }
});