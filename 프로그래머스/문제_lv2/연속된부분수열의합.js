function solution(sequence, k) {
  var answer = [];

  let acc = [0];
  let max = Infinity;
  sequence.forEach((num, i) => {
    acc.push(num + acc[i]);
  });

  let left = 0,
    right = 0;

  while (left <= right) {
    let sum = acc[right] - acc[left];
    if (sum === k) {
      let now = right - 1 - left;
      if (max > now) {
        answer = [left, right - 1];
        max = now;
      }
    }
    if (sum < k) right += 1;
    else left += 1;
  }

  return answer;
}
