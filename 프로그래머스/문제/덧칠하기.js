function solution(n, m, section) {
  var answer = 0;

  let start = section[0];
  answer += 1;

  for (const num of section) {
    if (start + m > num) {
      continue;
    }

    start = num;
    answer += 1;
  }

  return answer;
}
