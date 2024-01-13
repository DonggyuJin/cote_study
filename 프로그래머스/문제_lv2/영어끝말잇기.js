function solution(n, words) {
  var answer = [];

  let stack = [];
  let result = true;
  let idx = 1;
  let order = 1;

  for (let i = 0; i < words.length; i++) {
    if (i === 0) {
      idx += 1;
      stack.push(words[i]);
      continue;
    }
    if (idx > n) {
      idx = 1;
      order += 1;
    }
    if (
      words[i - 1][words[i - 1].length - 1] != words[i][0] ||
      stack.includes(words[i])
    ) {
      result = false;
      break;
    }
    idx += 1;
    stack.push(words[i]);
  }

  if (result) answer = [0, 0];
  else answer = [idx, order];

  return answer;
}
