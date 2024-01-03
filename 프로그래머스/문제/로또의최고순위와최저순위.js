function solution(lottos, win_nums) {
  var answer = [];

  const rank = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5 };

  let temp = 0;
  for (const lotto of lottos) {
    if (win_nums.includes(lotto)) {
      temp += 1;
    }
  }

  const zero = lottos.filter((lotto) => lotto === 0).length;

  if (temp === 0 && zero === 0) return [6, 6];
  if (zero === 0) return [rank[temp], rank[temp]];
  else {
    if (rank[temp]) {
      return [rank[temp + zero], rank[temp]];
    } else {
      return [rank[temp + zero], 6];
    }
  }

  return answer;
}
