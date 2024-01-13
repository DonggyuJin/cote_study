function solution(n) {
  var answer = 0;

  let arr = [];
  arr[0] = 1;
  arr[1] = 2;
  for (let i = 2; i <= 2000; i++) {
    arr[i] = (arr[i - 2] + arr[i - 1]) % 1234567;
  }

  answer = arr[n - 1];

  return answer;
}
