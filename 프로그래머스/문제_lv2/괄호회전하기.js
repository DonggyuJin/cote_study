function solution(s) {
  var answer = 0;

  let sArr = s.split("");
  let stack;
  for (let i = 0; i < s.length; i++) {
    stack = [];

    if (i > 0) {
      const temp = sArr.shift();
      sArr.push(temp);
    }

    for (let i = 0; i < sArr.length; i++) {
      stack.push(sArr[i]);
      if (stack.length >= 2) {
        // console.log(sArr, '->', stack);
        if (
          stack[stack.length - 2] === "{" &&
          stack[stack.length - 1] === "}"
        ) {
          stack.pop();
          stack.pop();
        } else if (
          stack[stack.length - 2] === "[" &&
          stack[stack.length - 1] === "]"
        ) {
          stack.pop();
          stack.pop();
        } else if (
          stack[stack.length - 2] === "(" &&
          stack[stack.length - 1] === ")"
        ) {
          stack.pop();
          stack.pop();
        }
      }
    }

    if (stack.length === 0) answer += 1;
  }

  return answer;
}
