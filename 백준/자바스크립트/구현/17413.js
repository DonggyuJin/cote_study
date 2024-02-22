const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

const str = input[0].split("");
let temp = "";
let result = "";

let idx = 0;
while (idx < str.length) {
  if (str[idx] === "<") {
    if (temp !== "") {
      temp = temp.replaceAll("<", "");
      const tempArr = temp.split(" ");
      for (let i = 0; i < tempArr.length; i++) {
        tempArr[i] = tempArr[i].split("").reverse().join("");
      }
      result += tempArr.join(" ");
      temp = "";
    }
    while (true) {
      if (str[idx] === ">") {
        result += ">";
        break;
      }
      result += str[idx];
      idx++;
    }
  } else {
    if (str[idx] === ">") continue;
    temp += str[idx];
  }
  idx++;
}

if (temp !== "") {
  const tempArr = temp.split(" ");
  for (let i = 0; i < tempArr.length; i++) {
    tempArr[i] = tempArr[i].split("").reverse().join("");
  }
  result += tempArr.join(" ");
  temp = "";
}
console.log(result);
