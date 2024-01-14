function solution(k, tangerine) {
  var answer = 0;

  let tanObj = {};
  for (const tan of tangerine) {
    if (tanObj[tan]) tanObj[tan] += 1;
    else tanObj[tan] = 1;
  }

  let arr = Object.entries(tanObj).sort((a, b) => b[1] - a[1]);

  for (const num of arr) {
    answer += 1;
    k = k - num[1];
    if (k <= 0) break;
  }

  return answer;
}
