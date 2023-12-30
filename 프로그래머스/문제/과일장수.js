function solution(k, m, score) {
  var answer = 0;

  let temp = [];
  score = score.sort((a, b) => b - a);
  for (let i = 0; i <= score.length - m; i += m) {
    temp.push(score.slice(i, i + m));
  }

  temp.map((arr) => {
    answer += arr[arr.length - 1] * m;
  });

  return answer;
}
