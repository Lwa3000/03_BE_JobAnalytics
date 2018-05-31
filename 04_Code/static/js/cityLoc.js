function buildPlot() {

    var url = "/bar";
    Plotly.d3.json(url, function(error, data) {
        if (error) return console.warn(error);

        var layout = {
                    // margin: { t: 50 },
                    title: "Number of Job Postings per City",
                    titlefont: {
                        // size: 24,
                        color: 'rgb(242,242,242)'
                      },
                    xaxis: {
                        // title: "City",
                        titlefont: {
                            // size: 14,
                            color: 'rgb(242,242,242)'
                          },
                        showgrid: false,
                        zeroline: true,
                        showline: true,
                        gridcolor: 'rgb(242,242,242)',
                        gridwidth: 2,
                        zerolinecolor: 'rgb(242,242,242)',
                        zerolinewidth: 2,
                        linecolor: 'rgb(242,242,242)',
                        linewidth: 2,
                        autotick: false,
                        ticks: 'outside',
                        // tick0: 0,
                        ticklen: 2,
                        tickwidth: 4,
                        tickcolor: 'rgb(242,242,242)',
                        tickfont: {
                            // size: 14,
                            color: 'rgb(242,242,242)'
                      },
                      tickangle: -45
                    },
                    yaxis: {
                        title: "# of Job Postings",
                        titlefont: {
                            // size: 14,
                            color: 'rgb(242,242,242)'
                          },
                        showgrid: false,
                        zeroline: true,
                        showline: true,
                        gridcolor: 'rgb(242,242,242)',
                        gridwidth: 2,
                        zerolinecolor: 'rgb(242,242,242)',
                        zerolinewidth: 2,
                        linecolor: 'rgb(242,242,242)',
                        linewidth: 2,
                        autotick: true,
                        ticks: 'outside',
                        // tick0: 0,
                        ticklen: 4,
                        tickwidth: 2,
                        tickcolor: 'rgb(242,242,242)',
                        tickfont: {
                            // size: 14,
                            color: 'rgb(242,242,242)'
                      }
                    },
                    paper_bgcolor: '#2e2e2e',
                    plot_bgcolor: 'rgba(0,0,0,0)'
        };

        Plotly.newPlot("bars", data, layout);
    
    });
}
 
 buildPlot();
 