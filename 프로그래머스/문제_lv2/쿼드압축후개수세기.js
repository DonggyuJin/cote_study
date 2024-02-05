function solution(arr) {
  var answer = { 0: 0, 1: 0 };

  const func = (y, x, length, arr, answer) => {
    let num = arr[y][x];

    if (length === 1) {
      answer[num] += 1;
      return;
    }

    let check = true;
    for (let i = y; i < y + length; i++) {
      for (let j = x; j < x + length; j++) {
        if (arr[i][j] !== num) {
          check = false;
          break;
        }
      }
    }

    if (check) {
      answer[num] += 1;
      return;
    }

    let half = length / 2;

    func(y, x, half, arr, answer);
    func(y + half, x, half, arr, answer);
    func(y, x + half, half, arr, answer);
    func(y + half, x + half, half, arr, answer);
  };

  func(0, 0, arr.length, arr, answer);

  return Object.values(answer);
}
