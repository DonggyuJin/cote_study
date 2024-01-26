function solution(n, t, m, p) {
  var answer = "";

  let temp = "";
  for (let i = 0; i < m * t; i++) {
    temp += i.toString(n);
  }

  let idx = p - 1;
  while (answer.length !== t) {
    answer += temp[idx].toUpperCase();
    idx += m;
  }

  return answer;
}
