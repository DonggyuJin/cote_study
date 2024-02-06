function solution(number, k) {
  var answer = "";

  let stack = [];
  let num = number.split("").reverse();

  while (num.length && k > 0) {
    stack.push(num.pop());
    while (stack[stack.length - 1] < num[num.length - 1] && k > 0) {
      stack.pop();
      k -= 1;
    }
  }

  if (k !== 0) stack = stack.slice(0, -k);

  answer = stack.join("") + num.reverse().join("");

  return answer;
}
