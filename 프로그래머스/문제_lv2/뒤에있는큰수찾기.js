function solution(numbers) {
  var answer = [];

  let stack = [];
  let result = Array(numbers.length).fill(-1);
  for (const num of numbers) {
    const lastIdx = stack.length - 1;

    if (num > stack[lastIdx]) {
      let backIdx = 0;

      while (num > stack[lastIdx - backIdx]) {
        if (result[lastIdx - backIdx] === -1) {
          result[lastIdx - backIdx] = num;
        }
        backIdx += 1;
      }
    }
    stack.push(num);
  }

  answer = result;

  return answer;
}
