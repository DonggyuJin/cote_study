function solution(n) {
  var ans = 1;

  while (n > 2) {
    const div = parseInt(n / 2);
    const rest = n % 2;
    if (rest === 1) ans += 1;
    n = div;
  }

  return ans;
}
