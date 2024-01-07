function solution(s) {
  var answer = "";

  const max = Math.max(...s.split(" ").map(Number));
  const min = Math.min(...s.split(" ").map(Number));
  answer = `${min} ${max}`;

  return answer;
}
