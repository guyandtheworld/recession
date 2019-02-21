// Custom JavaScript

$(function () {
    createGraph();
});

function createGraph() {

    d3.json("/data", function (error, response) {
        var parsedData = parseData(response);
        drawChart(parsedData);
    });

    function parseData(data) {
        var arr = [];
        for (index in data) {
            arr.push(
                {
                    date: new Date(index),
                    value: + data[index].DIFF
                });
        }
        return arr;
    }

    function drawChart(data) {
        var svgWidth = 600, svgHeight = 400;
        var margin = { top: 20, right: 20, bottom: 30, left: 50 };
        var width = svgWidth - margin.left - margin.right;
        var height = svgHeight - margin.top - margin.bottom;

        var svg = d3.select('svg')
            .attr("width", svgWidth)
            .attr("height", svgHeight);

        var g = svg.append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")"
            );

        var x = d3.time.scale().rangeRound([0, width]);
        var y = d3.scale.linear().rangeRound([height, 0]);

        var line = d3.svg.line()
            .x(function (d) { return x(d.date) })
            .y(function (d) { return y(d.value) })

        x.domain(d3.extent(data, function (d) { return d.date }));
        y.domain(d3.extent(data, function (d) { return d.value }));

        g.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x))
            .select(".domain")
            .remove();

        g.append("g")
            .call(d3.axisLeft(y))
            .append("text")
            .attr("fill", "#000")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", "0.71em")
            .attr("text-anchor", "end")
            .text("Price ($)");

    }
}