// Custom JavaScript

$(function () {
    createGraph();
});

function createGraph() {

    // REQUEST THE DATA
    d3.json("/data", function (error, quotes) {
        console.log(quotes);
    });
}