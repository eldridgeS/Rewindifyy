// visualizer.js
let audio;
let fft;

function setup() {
    createCanvas(windowWidth, windowHeight);
    audio = document.getElementById('audioPlayer');
    fft = new p5.FFT();
    fft.setInput(audio);
}

function draw() {
    background(200);
    let spectrum = fft.analyze();
    noStroke();
    fill(255, 0, 0); // Color of the bars
    for (let i = 0; i < spectrum.length; i++) {
        let x = map(i, 0, spectrum.length, 0, width);
        let h = -height + map(spectrum[i], 0, 255, height, 0);
        rect(x, height, width / spectrum.length, h);
    }
}
