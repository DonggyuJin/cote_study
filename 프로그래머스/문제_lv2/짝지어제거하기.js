function solution(s) {
  var answer = -1;

  let stack = [];
  const sArr = s.split("");

  for (const s of sArr) {
    if (stack.length > 1) {
      if (stack[stack.length - 1] === stack[stack.length - 2]) {
        stack.pop();
        stack.pop();
      }
    }
    stack.push(s);
  }

  if (stack[stack.length - 1] === stack[stack.length - 2]) {
    stack.pop();
    stack.pop();
  }

  answer = stack.length > 0 ? 0 : 1;

  return answer;
}
