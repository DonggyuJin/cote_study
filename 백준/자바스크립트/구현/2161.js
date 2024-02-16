const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n").map(Number);

const N = input[0];
const card = [];
for (let i = 1; i <= N; i++) card.push(i);

const result = [];
while (card.length > 1) {
  const a = card.shift();
  result.push(a);
  const b = card.shift();
  card.push(b);
}
result.push(card[0]);
console.log(result.join(" "));
