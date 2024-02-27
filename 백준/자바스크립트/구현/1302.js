const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

const N = Number(input.shift());

const dict = {};
for (let i = 0; i < N; i++) {
  if (dict[input[i]]) dict[input[i]] += 1;
  else dict[input[i]] = 1;
}

const sortBook = Object.entries(dict)
  .sort(([aa, a], [bb, b]) => {
    if (a === b) {
      return aa < bb ? -1 : aa == bb ? 0 : 1;
    }
    return b - a;
  })
  .reduce((r, [k, v]) => ({ ...r, [k]: v }), {});

console.log(Object.keys(sortBook)[0]);
