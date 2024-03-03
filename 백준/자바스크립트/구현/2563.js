const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

const N = Number(input.shift());
const pos = input;

const paper = Array.from(Array(101), () => Array(101).fill(0));

for (const p of pos) {
  const [x, y] = p.split(" ").map(Number);
  for (let i = x; i < x + 10; i++) {
    for (let j = y; j < y + 10; j++) {
      paper[i][j] = 1;
    }
  }
}

let result = 0;
paper.map((el) => (result += el.filter((el) => el === 1).length));
console.log(result);
