function solution(t, p) {
  var answer = 0;

  const pLen = p.length;
  for (let i = 0; i <= t.length - pLen; i++) {
    let temp = t.slice(i, i + pLen);
    if (temp <= p) {
      answer += 1;
    }
  }

  return answer;
}
