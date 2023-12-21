const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n").map(Number);

// let result = null;

// for (let i = 0; i < input.length - 1; i++) {
//   for (let j = i + 1; j < input.length; j++) {
//     const sum = input.reduce((pre, cur) => pre + cur, 0);

//     if (sum - input[i] - input[j] === 100) {
//       result = input.filter(
//         (height) => height !== input[i] && height !== input[j]
//       );
//       break;
//     }
//   }
// }

// console.log(result.sort((a, b) => a - b).join("\n"));

function getCombinations(arr, num) {
  const result = [];
  if (num === 1) return arr.map((e) => [e]);

  arr.forEach((e, i, origin) => {
    const rest = origin.slice(i + 1);
    const combination = getCombinations(rest, num - 1);
    const attached = combination.map((el) => [e, ...el]);
    result.push(...attached);
  });
  return result;
}

let result = [];

getCombinations(input, 7).forEach((comb) =>
  comb.reduce((pre, cur) => pre + cur) === 100 ? (result = comb) : null
);

console.log(result.sort((a, b) => a - b));
