const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs.readFileSync(path).toString().trim().split("\n");

while (true) {
  const N = Number(input.shift());

  if (N === 0) break;
  else {
    let arr = input.splice(0, N);
    arr = arr.map((el) => {
      let [name, num] = el.split(" ");
      num = Number(num);
      return (el = [name, num]);
    });
    arr.sort(([a, b], [c, d]) => d - b);

    const maxNum = arr[0][1];

    const nameArr = arr.filter((el) => {
      const [name, num] = el;
      return num === maxNum;
    });
    console.log(nameArr.map((el) => (el = el[0])).join(" "));
  }
}
