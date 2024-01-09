function solution(s) {
  var answer = true;

  let stack = [];

  for (let i = 0; i < s.length; i++) {
    if (stack.length < 0) {
      break;
    }
    if (stack[stack.length - 1] === "(" && s[i] === ")") {
      stack.pop();
    } else {
      stack.push(s[i]);
    }
  }

  answer = stack.length === 0;

  return answer;
}
