const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

const T = Number(input.shift());

for (let i = 0; i < T; i++) {
  const [M, N, K] = input.shift().split(" ").map(Number);
  let map = Array.from(Array(M), () => new Array(N).fill(0));
  for (let j = 0; j < K; j++) {
    let pos = input.shift().split(" ");
    map[pos[0]][pos[1]] = 1;
  }
}
