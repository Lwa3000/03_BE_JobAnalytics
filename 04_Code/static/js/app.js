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
                color: 'rgb(49,130,189)',
                opacity: 0.7
            }
        };

        var trace2 = {
            type: "bar",
            name: "San Francisco",
            x: response.map(data => data.skill_type),
            y: response.map(data => data.city2),
            marker: {
                color: 'rgb(204,204,204)',
                opacity: 0.5
              }
        };

        var data = [trace1, trace2];

        var layout = {
            title: 'Data Analyst Skills by City',
            xaxis: {
              tickangle: -45
            },
            barmode: 'group'
          };

        Plotly.newPlot("barplot", data, layout);
    });
}

buildPlot();
