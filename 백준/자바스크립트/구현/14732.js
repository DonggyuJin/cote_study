const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

const N = Number(input.shift());
const pos = input;

const map = Array.from(Array(501), () => Array(501).fill(0));

for (let i = 0; i < N; i++) {
  const [x1, y1, x2, y2] = pos[i].split(" ").map(Number);
  for (let j = x1; j < x2; j++) {
    for (let k = y1; k < y2; k++) {
      map[j][k] = 1;
    }
  }
}

let result = 0;
for (const m of map) {
  result += m.filter((el) => el === 1).length;
}

console.log(result);
