document.addEventListener("DOMContentLoaded", function () {
  const basePath = "/assets/json/team_data/";
  const defaultYear = 2024;
  const team1Select = document.getElementById("team1-select");
  const team2Select = document.getElementById("team2-select");
  const compareButton = document.getElementById("compare-btn");
  const comparisonResultsDiv = document.getElementById("comparison-results");
  const team1StatsDiv = document.getElementById("team1-stats");
  const team2StatsDiv = document.getElementById("team2-stats");
  const comparisonTableDiv = document.getElementById("comparison-table-div");
  const chartDiv = document.getElementById("chart-container");

  // Load available teams for 2024
  fetch(`/assets/json/team_data/team_abbrev_list_2024.json`)
    .then((response) => response.json())
    .then((teams) => populateTeamDropdowns(teams))
    .catch((error) => console.error("Failed to load teams:", error));

  // Compare teams when the button is clicked
  compareButton.addEventListener("click", function () {
    const team1 = team1Select.value;
    const team2 = team2Select.value;

    if (!team1 || !team2 || team1 === team2) {
      alert("Please select two different teams.");
      return;
    }

    // Fetch team data and display comparison
    Promise.all([
      fetch(`${basePath}${team1}_${defaultYear}_summary.json`).then((res) => res.json()),
      fetch(`${basePath}${team2}_${defaultYear}_summary.json`).then((res) => res.json()),
      fetch(`${basePath}${team1}_${defaultYear}_weekly_scores.json`).then((res) => res.json()),
      fetch(`${basePath}${team2}_${defaultYear}_weekly_scores.json`).then((res) => res.json()),
      fetch(`${basePath}${team1}_${defaultYear}_pie.json`).then((res) => res.json()),
      fetch(`${basePath}${team2}_${defaultYear}_pie.json`).then((res) => res.json())
    ])
      .then(([team1Summary, team2Summary, team1Weekly, team2Weekly, team1Pie, team2Pie]) => {
        const team1Name = team1Summary.name || team1;
        const team2Name = team2Summary.name || team2;
        displayComparison(team1Name, team1Summary, team2Name, team2Summary);
        renderChart(team1Name, team1Weekly, team2Name, team2Weekly);
        renderPieChart('team1-pie', team1Pie);
        renderPieChart('team2-pie', team2Pie);
      })
      .catch((error) => {
        console.error("Error fetching team data:", error);
        alert("Failed to load team data. Please try again.");
      });
  });
  function renderPieChart(containerId, data) {
    const chart = echarts.init(document.getElementById(containerId));
    chart.setOption(data);
  }
  // Populate team dropdowns
  function populateTeamDropdowns(teams) {
    const selects = [team1Select, team2Select];
    selects.forEach((select) => {
      select.innerHTML = '<option value="">Select Team</option>';
      teams.forEach((team) => {
        const option = document.createElement("option");
        option.value = team.abbrev;
        option.textContent = team.name;
        select.appendChild(option);
      });
    });
  }

  // Display comparison results
  function displayComparison(team1Name, team1Summary, team2Name, team2Summary) {
    comparisonResultsDiv.style.display = "block";


    // Display comparison table
    comparisonTableDiv.innerHTML = `
      <div class="card">
        <div class="card-header">
          <h5>${team1Name} vs ${team2Name}</h5>
        </div>
        <div class="card-body">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th>Category</th>
                <th>${team1Name}</th>
                <th>${team2Name}</th>
              </tr>
            </thead>
            <tbody>
              ${team1Summary.map((item, index) => {
                const team1Value = item.value;
                const team2Value = team2Summary[index].value || "N/A";
                return `
                  <tr>
                    <td>${item.category}</td>
                    <td>${team1Value}</td>
                    <td>${team2Value}</td>
                  </tr>
                `;
              }).join("")}
            </tbody>
          </table>
        </div>
      </div>
    `;
  }

  // Render the chart with combined data
  function renderChart(team1Name, team1Weekly, team2Name, team2Weekly) {
    const chart = echarts.init(chartDiv);

    const weeks = team1Weekly.xAxis.data; // Assuming both teams have the same weeks

    const option = {
      tooltip: {
        trigger: 'axis',
      },
      legend: {
        data: [
          `${team1Name} Points For`,
          `${team1Name} Points Against`,
          'League Avg',
          `${team2Name} Points For`,
          `${team2Name} Points Against`,
        ],
      },
      grid: {
        top: '10%',
        bottom: '5%',
        left: '6%',
        right: '0%',
      },
      xAxis: {
        type: 'category',
        data: weeks,
      },
      yAxis: {
        type: 'value',
        name: 'Points',
        nameLocation: 'center',
        nameGap: 35,
        nameTextStyle: {
          fontSize: 16,
        },
        axisLabel: {
          fontSize: 14,
        },
      },
      series: [
        {
          name: `${team1Name} Points For`,
          type: 'line',
          data: team1Weekly.series[0].data,
          symbol: 'circle',
          symbolSize: 8,
          lineStyle: {
            width: 3,
            color: '#FF6F61', // Custom color for Team 1 Points For
          },
        },
        {
          name: `${team1Name} Points Against`,
          type: 'line',
          data: team1Weekly.series[1].data,
          symbol: 'circle',
          symbolSize: 8,
          lineStyle: {
            width: 3,
            color: '#FFB84D', // Custom color for Team 1 Points Against
          },
        },
        {
          name: 'League Avg',
          type: 'line',
          data: team1Weekly.series[2].data,
          symbol: 'none',
          lineStyle: {
            type: 'dashed',
            width: 2,
            color: '#888', // Color for League Average
          },
        },
        {
          name: `${team2Name} Points For`,
          type: 'line',
          data: team2Weekly.series[0].data,
          symbol: 'circle',
          symbolSize: 8,
          lineStyle: {
            width: 3,
            color: '#3C8D40', // Custom color for Team 2 Points For
          },
        },
        {
          name: `${team2Name} Points Against`,
          type: 'line',
          data: team2Weekly.series[1].data,
          symbol: 'circle',
          symbolSize: 8,
          lineStyle: {
            width: 3,
            color: '#FFD700', // Custom color for Team 2 Points Against
          },
        },
      ],
    };

    chart.setOption(option);
  }
});
