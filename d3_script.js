console.log(d3); // test if d3 is loaded

var svg = d3.select('body').select('#vis')
    .attr('width', 800)
    .attr('height', 800)

var scale = d3.scaleLinear()
    .domain([0, 15000])
    .range([0, 1000])

// style='background-image: url("http:\\\\ddragon.leagueoflegends.com\\cdn\\6.8.1\\img\\map\\map11.png")'
fetch('http://localhost:8080/partFrame.csv', { 'Access-Control-Allow-Origin': '*' })
    .then(result => {
        return result.text();
    }).then(result => {
        console.log(result)
        var data = d3.csvParse(result)

        var circles = svg.selectAll('positions')
            .data(data)
            .enter()
            .append('circle')
            .attr('cx', d => d.x)
            .attr('cy', d => d.y)
            .attr('r', 10)
    })