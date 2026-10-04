/*
 * Conway's Game of Life, drawn faintly behind the page on <canvas class="life">
 * (see _layouts/default.html). The lab logo is a glider.
 *
 * - The grid wraps around at the edges; one generation every STEP_MS.
 * - Cells fade in and out over a few frames instead of blinking.
 * - A small random patch is dropped in when the board dies down or settles into
 *   still lifes and blinkers, and every REFRESH generations, so it keeps moving.
 * - Stops while the tab is hidden (requestAnimationFrame does), and shows one
 *   still frame for visitors who prefer reduced motion.
 * - Cell colour is the CSS `color` of the canvas (the --life variable), so it
 *   follows the light/dark theme.
 */
(function () {
  'use strict';

  var CELL = 12;          // cell size in CSS pixels
  var STEP_MS = 160;      // time per generation
  var FRAME_MS = 33;      // redraw at most ~30 times a second
  var DENSITY = 0.18;     // share of live cells in a fresh random patch
  var FADE = 0.25;        // how far a cell's shade moves towards its state per frame
  var LEVELS = 6;         // distinct shades drawn per frame
  var PATCH = 10;         // side of a reseeded patch, in cells
  var REFRESH = 250;      // also drop in a patch every this many generations

  var canvas = document.querySelector('canvas.life');
  if (!canvas || !canvas.getContext) return;
  var ctx = canvas.getContext('2d');
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  var cols = 0, rows = 0;
  var cells, next, shade;   // current state, scratch buffer, displayed shade (0..1)
  var hashes = [0, 0, 0];   // state fingerprints of the last generations
  var stuck = 0;            // generations in a row that repeat with period 1 or 2
  var generation = 0;
  var color = '';
  var lastStep = 0, lastFrame = 0, running = false;

  function seed(x0, y0, w, h, density) {
    for (var y = y0; y < y0 + h; y++) {
      for (var x = x0; x < x0 + w; x++) {
        if (Math.random() < density) cells[((y + rows) % rows) * cols + (x + cols) % cols] = 1;
      }
    }
  }

  // Size the canvas to the window. Live cells in the overlapping area survive,
  // so the mobile address bar showing and hiding doesn't restart the board.
  function resize() {
    var dpr = window.devicePixelRatio || 1;
    var width = window.innerWidth, height = window.innerHeight;
    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    var newCols = Math.ceil(width / CELL), newRows = Math.ceil(height / CELL);
    if (newCols === cols && newRows === rows) return;
    var old = cells, oldCols = cols, oldRows = rows;
    cols = newCols;
    rows = newRows;
    cells = new Uint8Array(cols * rows);
    next = new Uint8Array(cols * rows);
    shade = new Float32Array(cols * rows);
    if (old) {
      for (var y = 0; y < Math.min(rows, oldRows); y++) {
        for (var x = 0; x < Math.min(cols, oldCols); x++) {
          cells[y * cols + x] = shade[y * cols + x] = old[y * oldCols + x];
        }
      }
    } else {
      seed(0, 0, cols, rows, DENSITY);
    }
  }

  function step() {
    var alive = 0, hash = 0;
    for (var y = 0; y < rows; y++) {
      var up = ((y + rows - 1) % rows) * cols, mid = y * cols, down = ((y + 1) % rows) * cols;
      for (var x = 0; x < cols; x++) {
        var left = (x + cols - 1) % cols, right = (x + 1) % cols;
        var n = cells[up + left] + cells[up + x] + cells[up + right] +
                cells[mid + left] + cells[mid + right] +
                cells[down + left] + cells[down + x] + cells[down + right];
        var live = n === 3 || (n === 2 && cells[mid + x]) ? 1 : 0;
        next[mid + x] = live;
        if (live) {
          alive++;
          hash = (hash + Math.imul(mid + x + 1, 2654435761)) | 0;
        }
      }
    }
    var swap = cells;
    cells = next;
    next = swap;

    // Same state as one or two generations ago: only still lifes and blinkers left.
    stuck = hash === hashes[0] || hash === hashes[1] ? stuck + 1 : 0;
    hashes = [hash, hashes[0], hashes[1]];
    generation++;
    if (stuck > 8 || alive < cols * rows * 0.02 || generation % REFRESH === 0) {
      seed(Math.floor(Math.random() * cols), Math.floor(Math.random() * rows), PATCH, PATCH, 0.4);
      stuck = 0;
    }
  }

  function draw() {
    var width = cols * CELL, height = rows * CELL;
    ctx.clearRect(0, 0, width, height);
    var paths = [];
    for (var level = 1; level <= LEVELS; level++) paths.push(new Path2D());
    for (var i = 0; i < shade.length; i++) {
      var level = Math.round(shade[i] * LEVELS);
      if (level > 0) {
        paths[level - 1].rect((i % cols) * CELL + 1, Math.floor(i / cols) * CELL + 1, CELL - 2, CELL - 2);
      }
    }
    ctx.fillStyle = color;
    for (var l = 0; l < LEVELS; l++) {
      ctx.globalAlpha = (l + 1) / LEVELS;
      ctx.fill(paths[l]);
    }
    ctx.globalAlpha = 1;
  }

  function fade() {
    for (var i = 0; i < shade.length; i++) {
      var target = cells[i], value = shade[i];
      if (value !== target) {
        value += (target - value) * FADE;
        shade[i] = Math.abs(target - value) < 0.02 ? target : value;
      }
    }
  }

  function frame(now) {
    if (!running) return;
    if (now - lastStep >= STEP_MS) {
      step();
      lastStep = now;
    }
    if (now - lastFrame >= FRAME_MS) {
      fade();
      draw();
      lastFrame = now;
    }
    requestAnimationFrame(frame);
  }

  function readColor() {
    color = getComputedStyle(canvas).color;
  }

  function start() {
    if (reducedMotion.matches) {
      running = false;
      shade.set(cells);
      draw();
    } else if (!running) {
      running = true;
      requestAnimationFrame(frame);
    }
  }

  readColor();
  resize();
  start();

  window.addEventListener('resize', function () {
    resize();
    if (!running) draw();
  });
  document.addEventListener('themechange', function () {
    readColor();
    if (!running) draw();
  });
  reducedMotion.addEventListener('change', start);
})();
