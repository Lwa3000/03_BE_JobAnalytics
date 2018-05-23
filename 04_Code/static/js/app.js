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
                color: 'rgb(136,106,255)',
                opacity: 1
            }
        };

        var trace2 = {
            type: "bar",
            name: "San Francisco",
            x: response.map(data => data.skill_type),
            y: response.map(data => data.city2),
            marker: {
                color: 'rgb(106,225,255)',
                opacity: 1
              }
        };

        var data = [trace1, trace2];
        
        var layout = {
            xaxis: {tickfont: {
              color: 'rgb(107, 107, 107)'
            },
            tickangle: -45
          },
            yaxis: {
              title: 'Number of Jobs',
              titlefont: {
                size: 16,
                color: 'rgb(107, 107, 107)'
              },
              titlefont: {
                size: 16,
                color: 'rgb(107, 107, 107)'
              },
              tickfont: {
                size: 14,
                color: 'rgb(107, 107, 107)'
              }
            },
            barmode: 'group',
            bargap: 0.15,
            bargroupgap: 0.1
          };

        Plotly.newPlot("barplot", data, layout);
    });
}

buildPlot();
