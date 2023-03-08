// Chart for plot 1
var ctx1 = document.getElementById('myChart1').getContext('2d');

var graphData1 = {
    type: 'line',
    data: {
        labels: ['0','10','20','30','40','50'],
        datasets: [{
            label: 'ECG THARSIS',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(200,198,50,15)'
            ],
            borderColor: "#FFFFFF",
            borderWidth: 3
        }]
    },
      options: {}
}
    


var myChart1 = new Chart(ctx1, graphData1);

// Chart for plot 2
var ctx2 = document.getElementById('myChart2').getContext('2d');

var graphData2 = {
    type: 'line',
    data: {
        labels: ['0','10','20','30','40','50'],
        datasets: [{
            label: 'Second Dataset',
            data: [5, 10, 8, 15, 25, 20],
            backgroundColor: [
                'rgba(100,149,237,0.5)'
            ],
            borderColor: "#0000FF",
            borderWidth: 3
        }]
    },
    options: {}
}

var myChart2 = new Chart(ctx2, graphData2);

// WebSocket code
var socket = new WebSocket('ws://localhost:8000/ws/graph/');

socket.onmessage = function (e) {
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);


    // Modify dataset for plot 1
    var newGraphData1 = graphData1.data.datasets[0].data;
    newGraphData1.shift();
    newGraphData1.push(djangoData.PPG);

    graphData1.data.datasets[0].data = newGraphData1;
    myChart1.update();

    // Modify dataset for plot 2
    var newGraphData2 = graphData2.data.datasets[0].data;
    newGraphData2.shift();
    newGraphData2.push(djangoData.PPG * 2);

    graphData2.data.datasets[0].data = newGraphData2;
    myChart2.update();
    document.querySelector('#PPG').innerText = djangoData.PPG;
    document.querySelector('#oxigeno').innerText = djangoData.oxigeno;
    document.querySelector('#BPM').innerText = djangoData.BPM;
    document.querySelector('#aceleracion').innerText = djangoData.aceleracion;
    document.querySelector('#velocidad').innerText = djangoData.velocidad;



}
