function buildPlot() {

  var url = "/data";
  Plotly.d3.json(url, function(error, response) {

      console.log(response);

      var trace1 = {
          type: "bar",
          name: "New York",
          x: response.map(data => data.skill_type),
          y: response.map(data => data.city1),
          text: response.map(data => data.city1),
          textposition: "inside",
          textfont: {
            size: 9.5,
            color: 'black'
          },
          hoverinfo: "name+y",
          marker: {
            color: 'rgb(30, 210, 255)',
            opacity: 1
          }
      };

      var trace2 = {
          type: "bar",
          name: "San Francisco",
          x: response.map(data => data.skill_type),
          y: response.map(data => data.city2),
          text: response.map(data => data.city2),
          textposition: "inside",
          textfont: {
            size: 9.5,
            color: 'black'
          },
          hoverinfo: "name+y",
          marker: {
            color: 'rgb(247,54,185)',
            opacity: 1
            }
      };

      var data = [trace1, trace2];
      
      var layout = {
        title: 'Top 10 Skills in Demand',
        titlefont: {
          size: 24,
          color: 'rgb(242,242,242)'
        },
          xaxis: {
            range: [-0.5,9.5],
            showgrid: false,
            zeroline: true,
            showline: true,
            // mirror: 'ticks',
            gridcolor: 'rgb(242,242,242)',
            gridwidth: 2,
            zerolinecolor: 'rgb(242,242,242)',
            zerolinewidth: 2,
            linecolor: 'rgb(242,242,242)',
            linewidth: 2,
            autotick: true,
            ticks: 'outside',
            tick0: 0,
            // dtick: 10,
            ticklen: 2,
            tickwidth: 4,
            tickcolor: 'rgb(242,242,242)',
            tickfont: {
            size: 14,
            color: 'rgb(242,242,242)'
          },
          tickangle: -45
        },
          yaxis: {
            showgrid: false,
            zeroline: true,
            showline: true,
            // mirror: 'ticks',
            gridcolor: 'rgb(242,242,242)',
            gridwidth: 2,
            zerolinecolor: 'rgb(242,242,242)',
            zerolinewidth: 2,
            linecolor: 'rgb(242,242,242)',
            linewidth: 2,
            title: 'Number of Job Postings',
            titlefont: {
              size: 14,
              color: 'rgb(242,242,242)'
            },
            titlefont: {
              size: 14,
              color: 'rgb(242,242,242)'
            },
            autotick: true,
            ticks: 'outside',
            tick0: 0,
            // dtick: 10,
            ticklen: 4,
            tickwidth: 2,
            tickcolor: 'rgb(242,242,242)',
            tickfont: {
              size: 14,
              color: 'rgb(242,242,242)'
            }
          },
          legend: {
            font: {
              size: 14,
              color: 'rgb(242,242,242)'
            },
          },
          barmode: 'group',
          bargap: 0.2,
          bargroupgap: 0.1,
          paper_bgcolor: '#2e2e2e',
          plot_bgcolor: 'rgba(0,0,0,0)',
        };

      Plotly.newPlot("barplot", data, layout);
  });
}

buildPlot();
