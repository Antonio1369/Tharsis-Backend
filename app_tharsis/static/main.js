var ctx = document.getElementById('myChart').getContext('2d');

var graphData = {

    type: 'line',
    data: {
      labels: ['0','10','20','30','40','50','60','70','80','90','100','110','120','130','140','150','160','170','180'],
      datasets: [{
        label: 'ECG THARSIS',
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
            'rgba(200,198,50,0.5)'
        ],
        borderColor: "#FF0000",
        borderWidth: 3
      }]
    },
    options: {}
}

var myChart = new Chart(ctx,graphData);

var socket = new WebSocket('ws://localhost:8000/ws/graph/');

socket.onmessage = function (e){
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);
    var newGraphData = graphData.data.datasets[0].data;
    newGraphData.shift();
    newGraphData.push(djangoData.value);

    graphData.data.datasets[0].data = newGraphData;
    myChart.update()

    document.querySelector('#app').innerHTML =djangoData.value;

    
}