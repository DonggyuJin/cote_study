function solution(d, budget) {
  var answer = 0;

  d = d.sort((a, b) => a - b);
  for (const num of d) {
    if (num <= budget) {
      answer += 1;
      budget -= num;
    }
  }

  return answer;
}
