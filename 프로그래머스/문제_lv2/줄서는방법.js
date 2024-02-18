function solution(n, k) {
  var answer = [];

  const arr = Array.from(Array(n), (_, idx) => idx + 1);

  for (let i = 1; i <= n; i++) {
    let divider = 1;

    for (let j = 1; j <= n - i; j++) {
      divider *= j;
    }
    const idx = Math.ceil(k / divider) - 1;
    const pop = arr.splice(idx, 1)[0];
    answer.push(pop);
    k -= divider * idx;
  }

  return answer;
}
