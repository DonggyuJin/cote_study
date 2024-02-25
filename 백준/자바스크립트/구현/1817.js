const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);

if (N === 0) return console.log(0);

const boxs = input[0].split(" ").map(Number);

let result = 0;
let temp = 0;
for (const box of boxs) {
  if (temp + box > M) {
    temp = 0;
    result += 1;
  }
  temp += box;
}

if (temp !== 0) result += 1;

console.log(result);
