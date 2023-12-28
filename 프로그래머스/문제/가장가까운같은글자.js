function solution(s) {
  var answer = [];

  let obj = {};
  for (let i = 0; i < s.length; i++) {
    if (s[i] in obj) {
      answer.push(i - obj[s[i]]);
      obj[s[i]] = i;
      continue;
    }
    answer.push(-1);
    obj[s[i]] = i;
  }

  return answer;
}
