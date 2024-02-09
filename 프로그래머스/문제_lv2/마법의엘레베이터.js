function solution(storey) {
  var answer = 0;

  const list = [];
  while (storey !== 0) {
    list.push(storey % 10);
    storey = parseInt(storey / 10);
  }

  for (let i = 0; i < list.length; i++) {
    if (list[i] < 5) answer += list[i];
    else if (list[i] > 5) {
      answer += 10 - list[i];
      if (i + 1 < list.length) list[i + 1]++;
      else answer++;
    } else if (list[i] === 5) {
      answer += list[i];
      if (i + 1 < list.length && list[i + 1] >= 5) list[i + 1]++;
    } else return -1;
  }

  return answer;
}
