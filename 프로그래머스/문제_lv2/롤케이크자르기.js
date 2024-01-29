function solution(topping) {
  var answer = 0;

  const leng = topping.length;
  const left = {};
  const right = {};
  let leftCnt = 0;
  let rightCnt = 0;

  if (leng === 1) return 0;

  for (let i = 0; i < leng; i++) {
    if (left[topping[i]]) left[topping[i]] += 1;
    else {
      left[topping[i]] = 1;
      leftCnt += 1;
    }
  }

  for (let i = leng - 1; i >= 0; i--) {
    left[topping[i]] -= 1;
    if (left[topping[i]] === 0) leftCnt -= 1;

    if (right[topping[i]]) {
      right[topping[i]] += 1;
    } else {
      right[topping[i]] = 1;
      rightCnt += 1;
    }

    if (leftCnt === rightCnt) answer += 1;
  }

  return answer;
}
