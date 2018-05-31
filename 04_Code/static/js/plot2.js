// Plot 2: Breakdown of Data Analyst titles by Region

function buildPlot2() {
    /* data route */
    var url = "/api/view2_NY";
    Plotly.d3.json(url, function(error, response) {

        console.log(response);

        var data = [response]

        var layout = {
            title: "V2: Breakdown of Data Analyst titles NY",
            titlefont: {
                size: 16,
                color: 'rgb(242,242,242)'
            },
            legend: {
                font: {
                    color: 'rgb(242,242,242)'
                }
            },
            paper_bgcolor: '#2e2e2e',
            plot_bgcolor: 'rgba(0,0,0,0)'
            // width: 800 px
            // height: 500 px
        };

        Plotly.newPlot("plot", data, layout);
    });

    var url2 = "/api/view2_SF";
    Plotly.d3.json(url2, function(error, response) {

        console.log(response);

        var data = [response]

        var layout = {
            title: "V2: Breakdown of Data Analyst titles SF",
            titlefont: {
                size: 16,
                color: 'rgb(242,242,242)'
            },
            legend: {
                font: {
                    color: 'rgb(242,242,242)'
                }
            },
            paper_bgcolor: '#2e2e2e',
            plot_bgcolor: 'rgba(0,0,0,0)'
            // width: 800 px
            // height: 500 px
        };

        Plotly.newPlot("plot2", data, layout);
    });
}

buildPlot2();


  