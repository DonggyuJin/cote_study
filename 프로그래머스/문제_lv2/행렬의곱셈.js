function solution(arr1, arr2) {
  var answer = [[]];

  answer = Array.from(Array(arr1.length), () => Array().fill([]));
  let num = 0;
  for (let i = 0; i < arr1.length; i++) {
    for (let x = 0; x < arr2[0].length; x++) {
      for (let j = 0; j < arr1[0].length; j++) {
        num += arr1[i][j] * arr2[j][x];
      }
      answer[i].push(num);
      num = 0;
    }
  }

  return answer;
}
