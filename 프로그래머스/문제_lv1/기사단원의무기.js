function solution(number, limit, power) {
  var answer = 0;

  for (let i = 1; i <= number; i++) {
    let temp = 0;
    for (let j = 1; j * j <= i; j++) {
      if (j * j === i) temp += 1;
      else if (i % j === 0) temp += 2;
    }
    if (temp <= limit) {
      answer += temp;
    } else {
      answer += power;
    }
  }

  return answer;
}
