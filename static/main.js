var parsedData;

var svgWidth = 800, svgHeight = 400;
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
    .y(function (d) { return y(d.value) });


d3.json("/data", function (error, response) {

    data = [];
    for (index in response) {
        data.push(
            {
                date: new Date(index),
                value: + response[index].DIFF
            });
    }

    parsedData = data;

    x.domain(d3.extent(data, function (d) { return d.date }));
    y.domain(d3.extent(data, function (d) { return d.value }));

    g.append("g")
        .attr("transform", "translate(0," + height + ")")
        .attr("class", "x axis")
        .call(d3.svg.axis().orient('bottom').scale(x))
        .select(".domain")
        .remove();

    g.append("g")
        .call(d3.svg.axis().orient('left').scale(y))
        .append("text")
        .attr("fill", "#000")
        .attr("class", "y axis")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text("% Diff");

    g.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("class", "line")
        .attr("stroke", "steelblue")
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("stroke-width", 1.5)
        .attr("d", line);
});


function appendData(initial, forecasted) {

    return initial.concat(forecasted);
}


function forecastCurve() {
    d3.json("/forecast", function (error, response) {
        var forecastedData = [];
        for (stuff in response) {
            forecastedData.push(
                {
                    date: new Date(response[stuff].date),
                    value: response[stuff].value
                }
            );
        }


        data = appendData(parsedData, forecastedData);

        x.domain(d3.extent(data, function (d) { return d.date }));
        y.domain(d3.extent(data, function (d) { return d.value }));

        var svg = d3.select("svg").transition();

        svg.select(".line")
            .duration(750)
            .attr("d", line(data));
        svg.select(".x.axis") // change the x axis
            .duration(750)
            .call(d3.svg.axis().orient('bottom').scale(x))
        svg.select(".y.axis") // change the y axis
            .duration(750)
            .call(d3.svg.axis().orient('left').scale(y));
    });
}
