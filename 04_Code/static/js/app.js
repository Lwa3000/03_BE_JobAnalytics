function buildPlot() {

    var url = "/data";
    Plotly.d3.json(url, function(error, response) {

        console.log(response);

        var trace1 = {
            type: "bar",
            name: "New York",
            x: response.map(data => data.skill_type),
            y: response.map(data => data.city1),
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
            marker: {
                color: 'rgb(247,54,185)',
                opacity: 1
              }
        };

        var data = [trace1, trace2];
        
        var layout = {
          title: 'Skills in Demand',
          titlefont: {
            size: 24,
            color: 'rgb(242,242,242)'
          },
            xaxis: {tickfont: {
              size: 14,
              color: 'rgb(242,242,242)'
            },
            tickangle: -45
          },
            yaxis: {
              title: 'Number of Jobs',
              titlefont: {
                size: 16,
                color: 'rgb(242,242,242)'
              },
              titlefont: {
                size: 16,
                color: 'rgb(242,242,242)'
              },
              tickfont: {
                size: 14,
                color: 'rgb(242,242,242)'
              }
            },
            legend: {
              font: {
                size: 16,
                color: 'rgb(242,242,242)'
              },
            },
            barmode: 'group',
            bargap: 0.2,
            bargroupgap: 0.1,
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
          };

        Plotly.newPlot("barplot", data, layout);
    });
}

buildPlot();
