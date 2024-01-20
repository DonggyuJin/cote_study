function solution(numbers) {
  var answer = "";

  numbers = numbers.map(String).sort((a, b) => {
    if (a + b < b + a) return 1;
    if (a + b > b + a) return -1;
    if (a + b === b + a) return 0;
  });

  answer = numbers.join("");
  if (+answer === 0) return "0";

  return answer;
}
