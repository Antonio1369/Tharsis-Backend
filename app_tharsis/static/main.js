// Chart for plot 1
var ctx1 = document.getElementById('myChart1').getContext('2d');

var graphData1 = {
    type: 'line',
    data: {
        labels: Array(50).fill(''),
        datasets: [{
            label: 'ECG TRHARSIS',
            data: Array(50).fill(0),
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)', // modify this to change the line color
            ],
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            xAxes: [{
                ticks: {
                    display: false // hide x-axis labels
                }
            }]
        }
    }

};


var myChart1 = new Chart(ctx1, graphData1);

// Chart for plot 2
var ctx2 = document.getElementById('myChart2').getContext('2d');

var graphData2 = {
    type: 'line',
    data: {
        labels: Array(50).fill(''),
        datasets: [{
            label: 'OXIGENACION',
            data: Array(50).fill(0),
            backgroundColor: [
                'rgba(100,149,237,0.5)'
            ],
            borderColor: "#0000FF",
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            xAxes: [{
                ticks: {
                    display: false // hide x-axis labels
                }
            }]
        }
    }
}

var myChart2 = new Chart(ctx2, graphData2);

// WebSocket code coolocar la ip para una conexion local

//var socket = new WebSocket('ws://192.168.1.39:8000/ws/graph/');
var socket = new WebSocket('ws://localhost:8000/ws/graph/');

// variable globar para giroscopio
var lastGiroscopioUpdate = 0;
var lastPMedicosUpdate = 0;

//giroscopio 3d
import * as THREE from 'https://unpkg.com/three/build/three.module.js';

const container = document.getElementById('rover');

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( container.offsetWidth, container.offsetWidth);

//renderer.setSize( window.innerWidth, window.innerHeight );
container.appendChild( renderer.domElement );

// Create the car geometry
const carGeometry = new THREE.BoxGeometry(2, 1, 1);

// Create the car material
const carMaterial = new THREE.MeshBasicMaterial({ color: 0xff0000 });

// Combine the geometry and material into a Mesh object
const car = new THREE.Mesh(carGeometry, carMaterial);

// Add the car to the scene
scene.add(car);

camera.position.z = 5;


socket.onmessage = function (e) {
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);

    // Modify dataset for plot 1
    var newGraphData1 = graphData1.data.datasets[0].data;
    newGraphData1.shift();
    newGraphData1.push(djangoData.PPG);

    graphData1.data.datasets[0].data = newGraphData1;

    // Modify labels for plot 1
    var newLabels1 = graphData1.data.labels;
    newLabels1.shift();
    newLabels1.push(new Date().toLocaleTimeString()); // add current time to labels array

    graphData1.data.labels = newLabels1;

    myChart1.update();

    // Modify dataset for plot 2
    var newGraphData2 = graphData2.data.datasets[0].data;
    newGraphData2.shift();
    newGraphData2.push(djangoData.PPG * 2);

    graphData2.data.datasets[0].data = newGraphData2;

    // Modify labels for plot 2
    var newLabels2 = graphData2.data.labels;
    newLabels2.shift();
    newLabels2.push(new Date().toLocaleTimeString()); // add current time to labels array

    graphData2.data.labels = newLabels2;

    myChart2.update();

    // Update HTML elements with real-time data



    // Update giroscopio data every 2 seconds
    var currentTimestamp = new Date().getTime();
    if (!lastGiroscopioUpdate || currentTimestamp - lastGiroscopioUpdate >= 1000) {
        lastGiroscopioUpdate = currentTimestamp;
        document.querySelector('#aceleracion1').innerText = djangoData.aceleracion1;
        document.querySelector('#aceleracion2').innerText = djangoData.aceleracion2;
        document.querySelector('#aceleracion3').innerText = djangoData.aceleracion3;
        document.querySelector('#giroscopio1').innerText = djangoData.giroscopio1;
        document.querySelector('#giroscopio2').innerText = djangoData.giroscopio2;
        document.querySelector('#giroscopio3').innerText = djangoData.giroscopio3;
        car.rotation.x = djangoData.giroscopio1;
        car.rotation.y = djangoData.giroscopio2;
        car.rotation.z = djangoData.giroscopio3;
    }
    if (!lastPMedicosUpdate || currentTimestamp - lastPMedicosUpdate >= 1000) {
        lastPMedicosUpdate = currentTimestamp;
        document.querySelector('#PPG').innerText = djangoData.PPG;
        document.querySelector('#oxigeno').innerText = djangoData.oxigeno;
        document.querySelector('#BPM').innerText = djangoData.BPM;
    }


}

function animate() {
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
}
animate();


