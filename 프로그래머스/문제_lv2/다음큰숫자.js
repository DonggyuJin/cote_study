function solution(n) {
  var answer = 0;

  const res = n
    .toString(2)
    .split("")
    .filter((str) => str === "1").length;
  for (let i = n + 1; i <= 1000000; i++) {
    const resN = i
      .toString(2)
      .split("")
      .filter((str) => str === "1").length;

    if (res === resN) return i;
  }

  return answer;
}
