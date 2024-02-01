function solution(numbers) {
  var answer = [];

  for (let num of numbers) {
    if (num % 2 === 0) {
      answer.push(num + 1);
    } else {
      const numBinary = num.toString(2);
      const idx = numBinary.lastIndexOf("0");

      if (idx === -1) answer.push(parseInt("10" + numBinary.slice(1), 2));
      else {
        const value = numBinary.slice(0, idx) + "10" + numBinary.slice(idx + 2);
        answer.push(parseInt(value, 2));
      }
    }
  }

  return answer;
}
