function solution(numbers) {
  var answer = [];

  let numSet = new Set();
  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      numSet.add(numbers[i] + numbers[j]);
    }
  }

  answer = [...numSet].sort((a, b) => a - b);

  return answer;
}
