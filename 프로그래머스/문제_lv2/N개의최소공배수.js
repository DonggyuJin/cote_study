function solution(arr) {
  var answer = 1;

  arr.sort((a, b) => b - a);
  let div = false;
  let cnt = arr[0];

  while (!div) {
    div = arr.every((num) => cnt % num === 0);
    if (div) {
      answer = cnt;
      break;
    }
    cnt += 1;
  }

  return answer;
}
