// Playoff Simulator Logic

let currentStandings = [];
let gameSelections = {};
let playoffBracket = {};

function initializeSimulator(data) {
    window.simulatorData = data;
    currentStandings = JSON.parse(JSON.stringify(data.current_standings));
    gameSelections = {};
    
    renderGameSelections();
    updateStandings();
    generatePlayoffBracket();
}

function calculateAverageScore(teamId) {
    const team = window.simulatorData.current_standings.find(t => t.team_id === teamId);
    if (!team) return 0;
    
    const totalGames = team.wins + team.losses;
    if (totalGames === 0) return 0;
    
    return team.points_for / totalGames;
}

function autoCalculateScores(winnerId, loserId) {
    const winnerAvg = calculateAverageScore(winnerId);
    const loserAvg = calculateAverageScore(loserId);
    
    let winnerScore = winnerAvg;
    let loserScore;
    
    if (loserAvg > winnerAvg) {
        loserScore = Math.max(0, winnerAvg - 1);
    } else {
        loserScore = loserAvg;
    }
    
    return {
        winnerScore: parseFloat(winnerScore.toFixed(2)),
        loserScore: parseFloat(loserScore.toFixed(2))
    };
}

function renderGameSelections() {
    const container = document.getElementById('game-selections');
    const games = window.simulatorData.remaining_games;
    
    // Group games by week
    const gamesByWeek = {};
    games.forEach((game, globalIdx) => {
        if (!gamesByWeek[game.week]) {
            gamesByWeek[game.week] = [];
        }
        gamesByWeek[game.week].push({...game, globalIdx: globalIdx});
    });
    
    let html = '';
    Object.keys(gamesByWeek).sort((a, b) => a - b).forEach(week => {
        html += `<div class="week-section">`;
        html += `<div class="week-header">Week ${week}</div>`;
        
        gamesByWeek[week].forEach((game) => {
            const gameId = `w${game.week}_${game.globalIdx}`;
            const selection = gameSelections[gameId] || {};
            
            html += `
                <div class="game-card">
                    <div class="matchup-container">
                        <div class="team-card ${selection.winner === 'away' ? 'selected' : ''}" 
                             id="${gameId}_away_card"
                             onclick="selectWinner('${gameId}', 'away', ${game.away_id}, ${game.home_id})">
                            <div class="team-name">${game.away_team}</div>
                            <div class="score-section">
                                <div class="score-label">Score (Optional)</div>
                                <input type="number" 
                                       class="score-input" 
                                       id="${gameId}_away_score"
                                       placeholder="--"
                                       step="0.01"
                                       value="${selection.away_score || ''}"
                                       onclick="event.stopPropagation()"
                                       oninput="updateScore('${gameId}', 'away', this.value)">
                            </div>
                        </div>
                        
                        <div class="vs-divider">@</div>
                        
                        <div class="team-card ${selection.winner === 'home' ? 'selected' : ''}" 
                             id="${gameId}_home_card"
                             onclick="selectWinner('${gameId}', 'home', ${game.home_id}, ${game.away_id})">
                            <div class="location-badge">HOME</div>
                            <div class="team-name">${game.home_team}</div>
                            <div class="score-section">
                                <div class="score-label">Score (Optional)</div>
                                <input type="number" 
                                       class="score-input" 
                                       id="${gameId}_home_score"
                                       placeholder="--"
                                       step="0.01"
                                       value="${selection.home_score || ''}"
                                       onclick="event.stopPropagation()"
                                       oninput="updateScore('${gameId}', 'home', this.value)">
                            </div>
                        </div>
                    </div>
                </div>
            `;
        });
        
        html += `</div>`;
    });
    
    container.innerHTML = html;
}

function selectWinner(gameId, winner, winnerId, loserId) {
    // Initialize if needed
    if (!gameSelections[gameId]) {
        gameSelections[gameId] = {};
    }
    
    // Store selection
    gameSelections[gameId].winner = winner;
    gameSelections[gameId].winner_id = winnerId;
    gameSelections[gameId].loser_id = loserId;
    
    // Auto-calculate scores
    const scores = autoCalculateScores(winnerId, loserId);
    
    // Store scores based on who won
    if (winner === 'away') {
        gameSelections[gameId].away_score = scores.winnerScore;
        gameSelections[gameId].home_score = scores.loserScore;
    } else {
        gameSelections[gameId].home_score = scores.winnerScore;
        gameSelections[gameId].away_score = scores.loserScore;
    }
    
    // Update the visual state for this specific card
    const awayCard = document.getElementById(`${gameId}_away_card`);
    const homeCard = document.getElementById(`${gameId}_home_card`);
    const awayScoreInput = document.getElementById(`${gameId}_away_score`);
    const homeScoreInput = document.getElementById(`${gameId}_home_score`);
    
    if (awayCard && homeCard) {
        awayCard.classList.remove('selected');
        homeCard.classList.remove('selected');
        
        if (winner === 'away') {
            awayCard.classList.add('selected');
        } else {
            homeCard.classList.add('selected');
        }
    }
    
    // Update score inputs
    if (awayScoreInput) {
        awayScoreInput.value = gameSelections[gameId].away_score || '';
    }
    if (homeScoreInput) {
        homeScoreInput.value = gameSelections[gameId].home_score || '';
    }
    
    updateStandings();
    generatePlayoffBracket();
}

function updateScore(gameId, team, value) {
    if (!gameSelections[gameId]) {
        gameSelections[gameId] = {};
    }
    
    const scoreValue = parseFloat(value) || null;
    
    if (team === 'away') {
        gameSelections[gameId].away_score = scoreValue;
    } else {
        gameSelections[gameId].home_score = scoreValue;
    }
    
    // Only update if there's a winner selected
    if (gameSelections[gameId].winner) {
        updateStandings();
        generatePlayoffBracket();
    }
}

function updateStandings() {
    // Start with current standings
    currentStandings = JSON.parse(JSON.stringify(window.simulatorData.current_standings));
    
    // Apply game selections
    Object.keys(gameSelections).forEach(gameId => {
        const selection = gameSelections[gameId];
        if (selection.winner) {
            const winner = currentStandings.find(t => t.team_id === selection.winner_id);
            const loser = currentStandings.find(t => t.team_id === selection.loser_id);
            
            if (winner && loser) {
                winner.wins++;
                loser.losses++;
                
                // Add scores if provided
                if (selection.winner === 'away' && selection.away_score) {
                    winner.points_for += selection.away_score;
                }
                if (selection.winner === 'home' && selection.home_score) {
                    winner.points_for += selection.home_score;
                }
                
                // Add loser's score
                if (selection.winner === 'away' && selection.home_score) {
                    loser.points_for += selection.home_score;
                }
                if (selection.winner === 'home' && selection.away_score) {
                    loser.points_for += selection.away_score;
                }
            }
        }
    });
    
    // Sort by wins (desc), then points_for (desc)
    currentStandings.sort((a, b) => {
        if (b.wins !== a.wins) return b.wins - a.wins;
        return b.points_for - a.points_for;
    });
    
    renderStandings();
}

function renderStandings() {
    const tbody = document.getElementById('standings-body');
    if (!tbody) return;
    
    const playoffTeams = window.simulatorData.playoff_config.playoff_teams;
    const byeTeams = window.simulatorData.playoff_config.bye_teams;
    
    let html = '';
    currentStandings.forEach((team, idx) => {
        const seed = idx + 1;
        let statusClass = '';
        let statusHTML = '';
        
        if (seed <= byeTeams) {
            statusClass = 'on-bye';
            statusHTML = '<span class="status-badge status-bye">🏆 FIRST ROUND BYE</span>';
        } else if (seed <= playoffTeams) {
            statusClass = 'in-playoffs';
            statusHTML = '<span class="status-badge status-playoff">✅ PLAYOFFS</span>';
        } else {
            statusHTML = '<span class="status-badge status-out">❌ ELIMINATED</span>';
        }
        
        html += `
            <tr class="${statusClass}">
                <td><strong style="font-size: 18px;">${seed}</strong></td>
                <td><strong>${team.team_name}</strong></td>
                <td>${team.wins}-${team.losses}</td>
                <td>${team.points_for.toFixed(2)}</td>
                <td>${statusHTML}</td>
            </tr>
        `;
    });
    
    tbody.innerHTML = html;
}

function generatePlayoffBracket() {
    const container = document.getElementById('bracket-container');
    if (!container) return;
    
    const playoffTeams = window.simulatorData.playoff_config.playoff_teams;
    const byeTeams = window.simulatorData.playoff_config.bye_teams;
    
    // Get playoff seeds based on current standings
    const seeds = currentStandings.slice(0, playoffTeams);
    const byeSeeds = seeds.slice(0, byeTeams);
    const wildCardSeeds = seeds.slice(byeTeams);
    
    // Wild Card Round (3v6, 4v5)
    const wildCardGames = [
        { home: wildCardSeeds[0], away: wildCardSeeds[3] },  // 3v6
        { home: wildCardSeeds[1], away: wildCardSeeds[2] }   // 4v5
    ];
    
    // For semifinals, assume higher seeds win (can be enhanced later)
    const wcWinners = [wildCardSeeds[0], wildCardSeeds[1]];
    
    // Reseed for semifinals
    const semiSeeds = [...byeSeeds, ...wcWinners].sort((a, b) => {
        const seedA = seeds.findIndex(s => s.team_id === a.team_id) + 1;
        const seedB = seeds.findIndex(s => s.team_id === b.team_id) + 1;
        return seedA - seedB;
    });
    
    const semiGames = [
        { home: semiSeeds[0], away: semiSeeds[3] },  // 1 vs lowest
        { home: semiSeeds[1], away: semiSeeds[2] }   // 2 vs next
    ];
    
    let html = `
        <div class="bracket">
            <div class="bracket-round">
                <div class="round-title">Wild Card</div>
                ${wildCardGames.map((game, idx) => `
                    <div class="bracket-game">
                        <div class="bracket-team">
                            <span><span class="seed-badge">${seeds.findIndex(s => s.team_id === game.home.team_id) + 1}</span>${game.home.team_name}</span>
                        </div>
                        <div class="bracket-team">
                            <span><span class="seed-badge">${seeds.findIndex(s => s.team_id === game.away.team_id) + 1}</span>${game.away.team_name}</span>
                        </div>
                    </div>
                `).join('')}
                <div class="bracket-game">
                    <div class="bye-indicator">
                        <span class="seed-badge">1</span>${byeSeeds[0].team_name}<br>FIRST ROUND BYE
                    </div>
                </div>
                <div class="bracket-game">
                    <div class="bye-indicator">
                        <span class="seed-badge">2</span>${byeSeeds[1].team_name}<br>FIRST ROUND BYE
                    </div>
                </div>
            </div>
            
            <div class="bracket-round">
                <div class="round-title">Semifinals</div>
                ${semiGames.map((game, idx) => `
                    <div class="bracket-game">
                        <div class="bracket-team">
                            <span><span class="seed-badge">${seeds.findIndex(s => s.team_id === game.home.team_id) + 1}</span>${game.home.team_name}</span>
                        </div>
                        <div class="bracket-team">
                            <span><span class="seed-badge">${seeds.findIndex(s => s.team_id === game.away.team_id) + 1}</span>${game.away.team_name}</span>
                        </div>
                    </div>
                `).join('')}
            </div>
            
            <div class="bracket-round">
                <div class="round-title">Championship</div>
                <div class="bracket-game">
                    <div class="bracket-team">
                        <span><span class="seed-badge">?</span>TBD</span>
                    </div>
                    <div class="bracket-team">
                        <span><span class="seed-badge">?</span>TBD</span>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    container.innerHTML = html;
}

function resetSimulator() {
    gameSelections = {};
    currentStandings = JSON.parse(JSON.stringify(window.simulatorData.current_standings));
    renderGameSelections();
    updateStandings();
    generatePlayoffBracket();
}

function calculateOptimalProjectedScore(teamId, week) {
    // Use week-specific optimal projections if available
    if (window.simulatorData.weekly_optimal_projections && 
        window.simulatorData.weekly_optimal_projections[week] &&
        window.simulatorData.weekly_optimal_projections[week][teamId]) {
        return window.simulatorData.weekly_optimal_projections[week][teamId];
    }
    
    // Fallback to average if week-specific not available
    return calculateAverageScore(teamId);
}

function simulateAllGames(method) {
    const games = window.simulatorData.remaining_games;
    
    // Clear existing selections first
    gameSelections = {};
    
    // Process all games and store selections
    games.forEach((game, idx) => {
        const gameId = `w${game.week}_${idx}`;
        
        let winner, winnerId, loserId;
        let winnerScore, loserScore;
        
        if (method === 'random') {
            winner = Math.random() > 0.5 ? 'home' : 'away';
            winnerId = winner === 'home' ? game.home_id : game.away_id;
            loserId = winner === 'home' ? game.away_id : game.home_id;
            
        } else if (method === 'favorite') {
            const homeTeam = window.simulatorData.current_standings.find(t => t.team_id === game.home_id);
            const awayTeam = window.simulatorData.current_standings.find(t => t.team_id === game.away_id);
            
            winner = homeTeam.points_for > awayTeam.points_for ? 'home' : 'away';
            winnerId = winner === 'home' ? game.home_id : game.away_id;
            loserId = winner === 'home' ? game.away_id : game.home_id;
        }
        
        // Use average scores for auto-calculation
        const winnerAvg = calculateAverageScore(winnerId);
        const loserAvg = calculateAverageScore(loserId);
        winnerScore = winnerAvg;
        loserScore = loserAvg > winnerAvg ? winnerAvg - 1 : loserAvg;
        
        // Store everything in gameSelections
        gameSelections[gameId] = {
            winner: winner,
            winner_id: winnerId,
            loser_id: loserId,
            away_score: winner === 'away' ? parseFloat(winnerScore.toFixed(2)) : parseFloat(loserScore.toFixed(2)),
            home_score: winner === 'home' ? parseFloat(winnerScore.toFixed(2)) : parseFloat(loserScore.toFixed(2))
        };
    });
    
    // Force a complete re-render of all game selections
    renderGameSelections();
    
    // Update standings and bracket
    updateStandings();
    generatePlayoffBracket();
}