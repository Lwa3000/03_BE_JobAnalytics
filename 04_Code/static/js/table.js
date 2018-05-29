function buildPlot() {

    var url = "/data";
    Plotly.d3.json(url, function(error, response) {

        console.log(response);
    
        var values = [
            (response.map(data => data.skill_type)),
            (response.map(data => data.city1_perc)),
            (response.map(data => data.city2_perc))
        ];
        var headerColor = "grey";
        var rowEvenColor = "lightgrey";
        var rowOddColor = "white";

        var data = [{
        type: 'table',
        columnwidth: [200,500,500],
        header: {
            values: [["<b>SKILL</b>"], 
                    ["<b>NEW YORK</b>"], 
                    ["<b>SAN FRANCISCO</b>"]],
            align: "center",
            line: {
                width: 1, 
                color: "rgb(242,242,242)"
            },
            fill: {
                color: '#3a3a3a',
                opacity: 0.5
            },
            font: {
                size: 16, 
                color: "rgb(242,242,242)"
            }
        },
        cells: {
            values: values,
            align: "center",
            // line: {color: "white", width: 1},
            fill: {color: 'rgba(0,0,0,0)'},
            font: {
                size: 14, 
                color: "rgb(242,242,242)"
            } 
        }}]

        var layout = {
            title: 'Percentage of Jobs with Technical Skill Mentioned',
            titlefont: {
                size: 24,
                color: 'rgb(242,242,242)'
              },
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: '#2e2e2e'
        };

    Plotly.plot('table', data, layout);
        });
    }

buildPlot();