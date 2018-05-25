function buildPlot() {

    var url = "/bar";
    Plotly.d3.json(url, function(error, data) {
        if (error) return console.warn(error);

        var layout = {
                    margin: { t: 50 },
                    title: "Number of Job Postings per City",
                    xaxis: { title: "City"},
                    yaxis: { title: "# of Job Postings"}
        };

        Plotly.newPlot("bars", data, layout);
    
    });
}
 
 buildPlot();
 