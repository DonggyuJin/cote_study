function solution(brown, yellow) {
  var answer = [];

  // 2X^2 + (4-brown)X + 2yellow = 0
  const x =
    ((brown - 4) / 2 + Math.sqrt(Math.pow((brown - 4) / 2, 2) - 4 * yellow)) /
    2;
  const y = yellow / x;

  answer = [Math.max(x + 2, y + 2), Math.min(x + 2, y + 2)];

  return answer;
}
