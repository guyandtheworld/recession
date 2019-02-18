// Custom JavaScript

$(function () {
    console.log('jquery is working!');
    createGraph();
});

function createGraph() {
    // Code goes here
    var width = 960; // chart width
    var height = 700; // chart height
    var format = d3.format(",d");  // convert value to integer
    var color = d3.scale.category20();  // create ordinal scale with 20 colors
    var sizeOfRadius = d3.scale.pow().domain([-100, 100]).range([-50, 50]);  // https://github.com/mbostock/d3/wiki/Quantitative-Scales#pow

    var bubble = d3.layout.pack()
        .sort(null)  // disable sorting, use DOM tree traversal
        .size([width, height])  // chart layout size
        .padding(1)  // padding between circles
        .radius(function (d) { return 20 + (sizeOfRadius(d) * 60); });  // radius for each circle

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

    // tooltip config
    var tooltip = d3.select("body")
        .append("div")
        .style("position", "absolute")
        .style("z-index", "10")
        .style("visibility", "hidden")
        .style("color", "white")
        .style("padding", "8px")
        .style("background-color", "rgba(0, 0, 0, 0.75)")
        .style("border-radius", "6px")
        .style("font", "12px sans-serif")
        .text("tooltip");

    node.append("circle")
        .attr("r", function (d) { return d.r; })
        .style('fill', function (d) { return color(d.symbol); })

        .on("mouseover", function (d) {
            tooltip.text(d.name + ": $" + d.price);
            tooltip.style("visibility", "visible");
        })
        .on("mousemove", function () {
            return tooltip.style("top", (d3.event.pageY - 10) + "px").style("left", (d3.event.pageX + 10) + "px");
        })
        .on("mouseout", function () { return tooltip.style("visibility", "hidden"); });
}
