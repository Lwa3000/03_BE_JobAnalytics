// Plot 2: Breakdown of Data Analyst titles by Region

function buildPlot2() {
    /* data route */
    var url = "/api/view2_NY";
    Plotly.d3.json(url, function(error, response) {

        console.log(response);

        var data = [response]

        var layout = {
            title: "V2: Breakdown of Data Analyst titles NY"
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
            title: "V2: Breakdown of Data Analyst titles SF"
            // width: 800 px
            // height: 500 px
        };

        Plotly.newPlot("plot2", data, layout);
    });
}

buildPlot2();


  