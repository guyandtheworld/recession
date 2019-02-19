// Custom JavaScript

$(function () {
    console.log('jquery is working!');
    createGraph();
});

function createGraph() {
    // Code goes here
    var width = 1600; // chart width
    var height = 600; // chart height
    var format = d3.format(",d");  // convert value to integer
    var color = d3.scale.category20();  // create ordinal scale with 20 colors
    var sizeOfRadius = d3.scale.pow().domain([-100, 100]).range([-50, 50]);  // https://github.com/mbostock/d3/wiki/Quantitative-Scales#pow

    var bubble = d3.layout.pack()
        .sort(null)  // disable sorting, use DOM tree traversal
        .size([width, height])  // chart layout size
        .padding(1)  // padding between circles
        .radius(function (d) { return 20 + (sizeOfRadius(d) * 30); });  // radius for each circle

    var svg = d3.select("#chart").append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("class", "bubble");

    // REQUEST THE DATA
    d3.json("/data", function (error, quotes) {
        var node = svg.selectAll('.node')
            .data(bubble.nodes(quotes)
                .filter(function (d) { return !d.children; }))
            .enter().append('g')
            .attr('class', 'node')
            .attr('transform', function (d) { return 'translate(' + d.x + ',' + d.y + ')' });

        node.append('circle')
            .attr('r', function (d) { return d.r; })
            .style('fill', function (d) { return color(d.symbol); });

        node.append('text')
            .attr("dy", ".3em")
            .style('text-anchor', 'middle')
            .text(function (d) { return d.symbol; });
    });

    d3.json("/data", function (error, quotes) {

    });

}
