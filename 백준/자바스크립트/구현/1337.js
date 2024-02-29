const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

let str = input[0];

str = str.replaceAll("s=", "1");
str = str.replaceAll("c=", "1");
str = str.replaceAll("c-", "1");
str = str.replaceAll("dz=", "1");
str = str.replaceAll("d-", "1");
str = str.replaceAll("lj", "1");
str = str.replaceAll("nj", "1");
str = str.replaceAll("z=", "1");

console.log(str.length);
