const container = document.getElementById('canvas-container');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
container.appendChild(renderer.domElement);

// 3D Wireframe Torus Knot
const geometry = new THREE.TorusKnotGeometry(2.5, 0.6, 100, 16);
const material = new THREE.MeshNormalMaterial({
    wireframe: true,
    transparent: true,
    opacity: 0.35
});

const torusKnot = new THREE.Mesh(geometry, material);
scene.add(torusKnot);

camera.position.z = 7;

let mouseX = 0;
let mouseY = 0;

window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 0.8;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 0.8;
});

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

function animate() {
    requestAnimationFrame(animate);

    torusKnot.rotation.x += 0.003;
    torusKnot.rotation.y += 0.005;

    torusKnot.rotation.x += (mouseY - torusKnot.rotation.x) * 0.02;
    torusKnot.rotation.y += (mouseX - torusKnot.rotation.y) * 0.02;

    renderer.render(scene, camera);
}
animate();
