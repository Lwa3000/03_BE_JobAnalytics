// Plot 2: Breakdown of Data Analyst titles by Region

function buildPlot2() {
    /* data route */
    var url = "/api/view2";
    Plotly.d3.json(url, function(error, response) {

        console.log(response);

        var data = [response]

        var layout = {
            title: "V2: Breakdown of Data Analyst titles by Region",
            width: 800
            height: 500
        };

        Plotly.newPlot("plot", data, layout);
    });
}

buildPlot2();


  