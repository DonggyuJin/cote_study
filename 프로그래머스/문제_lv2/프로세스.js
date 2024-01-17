function solution(priorities, location) {
  var answer = 0;

  const data = priorities.map((prior, idx) => ({ prior, idx }));

  while (data.length !== 0) {
    const max = Math.max(...priorities);
    const { prior, idx } = data.shift();

    if (prior >= max) {
      answer += 1;
      priorities[idx] = 1;
      if (idx === location) break;
    } else {
      data.push({ prior, idx });
    }
  }

  return answer;
}
