function solution(s) {
  var answer = [];

  let set = new Set();
  s = s
    .split("},{")
    .map((str) => str.replaceAll("{", "").replaceAll("}", "").split(","))
    .sort((a, b) => a.length - b.length)
    .forEach((arr) => arr.forEach((el) => set.add(el)));

  answer = [...set].map(Number);

  return answer;
}
