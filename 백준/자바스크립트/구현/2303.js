const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

const N = Number(input.shift());

const getCombinations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((el) => [fixed, ...el]);
    results.push(...attached);
  });

  return results;
};

const peoples = [];
for (let i = 0; i < N; i++) {
  peoples.push(input[i].split(" ").map(Number));
}

const maxNum = (arr) => {
  const numArray = getCombinations(arr, 3)
    .map((el) => {
      const str = (el = el.reduce((sum, cur) => sum + cur, 0)).toString();
      return Number(str[str.length - 1]);
    })
    .sort((a, b) => b - a);

  return numArray[0];
};

const numPeoples = [];
for (let i = 0; i < N; i++) {
  numPeoples.push(maxNum(peoples[i]));
}

const maxNumber = Math.max(...numPeoples);

const results = [];
for (let i = 0; i < N; i++) {
  if (numPeoples[i] === maxNumber) results.push(i + 1);
}

results.sort((a, b) => b - a);
console.log(results[0]);
