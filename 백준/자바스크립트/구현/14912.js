const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

const [n, num] = input[0].split(" ").map(Number);
let digit = "";
for (let i = 1; i <= n; i++) digit += i.toString();

console.log(digit.split("").filter((el) => el === num.toString()).length);
