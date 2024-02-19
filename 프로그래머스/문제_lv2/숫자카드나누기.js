function solution(arrayA, arrayB) {
  var answer = 0;

  let num1 = 500001;
  while (num1 > 0) {
    let b1 = true;
    let b2 = true;
    for (let i = 0; i < arrayA.length; i++) {
      if (arrayA[i] % num1 !== 0) b1 = false;
      if (arrayB[i] % num1 === 0) b2 = false;
      if (!b1 || !b2) break;
    }
    if (b1 && b2) break;
    num1--;
  }

  let num2 = 500001;
  while (num2 > 0) {
    let b1 = true;
    let b2 = true;
    for (let i = 0; i < arrayA.length; i++) {
      if (arrayA[i] % num2 === 0) b1 = false;
      if (arrayB[i] % num2 !== 0) b2 = false;
      if (!b1 || !b2) break;
    }
    if (b1 && b2) break;
    num2--;
  }

  answer = Math.max(num1, num2);

  return answer;
}
