function solution(weights) {
  var answer = 0;

  const dict = {};
  for (const weight of weights) {
    if (dict[weight] === undefined) dict[weight] = 1;
    else dict[weight] += 1;
  }

  weights.sort((a, b) => a - b);

  for (const weight of weights) {
    if (dict[weight] > 1) answer += dict[weight] - 1;
    if (dict[weight * (3 / 2)] > 0) answer += dict[weight * (3 / 2)];
    if (dict[weight * 2] > 0) answer += dict[weight * 2];
    if (dict[weight * (4 / 3)] > 0) answer += dict[weight * (4 / 3)];

    dict[weight] -= 1;
  }

  return answer;
}
