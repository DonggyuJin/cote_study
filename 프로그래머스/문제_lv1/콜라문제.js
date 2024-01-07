function solution(a, b, n) {
  var answer = 0;

  while (n >= a) {
    const qu = parseInt(n / a);
    const re = n % a;
    const cola = qu * b;

    answer += cola;
    n = cola + re;
  }

  return answer;
}
