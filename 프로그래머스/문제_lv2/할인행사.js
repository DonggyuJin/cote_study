function solution(want, number, discount) {
  var answer = 0;

  let disArr = [];
  for (let i = 0; i < discount.length - 9; i++) {
    disArr.push(discount.slice(i, i + 10));
  }

  for (const dis of disArr) {
    let temp = 0;
    for (let i = 0; i < want.length; i++) {
      if (dis.filter((el) => el === want[i]).length === number[i]) temp += 1;
    }
    if (temp === want.length) answer += 1;
  }

  return answer;
}
