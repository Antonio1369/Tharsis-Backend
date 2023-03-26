import * as THREE from 'https://unpkg.com/three/build/three.module.js';
//const container = document.getElementById('rover');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );
//container.appendChild( renderer.domElement );
const geometry = new THREE.BoxGeometry( 1, 1, 1 );
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 5;

//conection of websocket
var socket = new WebSocket('ws://localhost:8000/ws/graph/');

// listen for WebSocket messages
socket.onmessage = function(event) {
  const data = JSON.parse(event.data);
  console.log("este es el scrip.js")
  console.log(data);

  if (data.giroscopio1 !== undefined && data.giroscopio2 !== undefined && data.giroscopio3 !== undefined) {
    // update the rotation of the cube based on gyroscope data
    cube.rotation.x = data.giroscopio1;
    cube.rotation.y = data.giroscopio2;
    cube.rotation.z = data.giroscopio3;
  }

}

function animate() {
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
}

animate();
