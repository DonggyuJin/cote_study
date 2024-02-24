const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const pos = input;

const maps = Array.from(Array(101), () => Array(101).fill(0));
for (let i = 0; i < N; i++) {
  const [x1, y1, x2, y2] = pos[i].split(" ").map(Number);
  for (let i = x1; i <= x2; i++) {
    for (let j = y1; j <= y2; j++) {
      maps[i][j]++;
    }
  }
}

let result = 0;
maps.map((el) => (result += el.filter((e) => e > M).length));
console.log(result);
