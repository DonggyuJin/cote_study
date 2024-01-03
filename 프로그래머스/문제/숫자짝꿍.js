function solution(X, Y) {
  let answer = "";
  X = X.split("");
  Y = Y.split("");

  for (let i = 0; i < 10; i++) {
    const x = X.filter((a) => +a === i).length;
    const y = Y.filter((a) => +a === i).length;
    answer += String(i).repeat(Math.min(x, y));
  }

  if (answer === "") return "-1";
  if (+answer === 0) return "0";
  return answer
    .split("")
    .sort((a, b) => +b - +a)
    .join("");
}
