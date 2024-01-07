function solution(friends, gifts) {
  var answer = 0;

  let dict = {};
  for (let i = 0; i < friends.length; i++) {
    dict[friends[i]] = i;
  }

  let score = Array(friends.length).fill(0);
  let table = Array.from(Array(friends.length), () =>
    Array(friends.length).fill(0)
  );

  for (let i = 0; i < gifts.length; i++) {
    const [give, gave] = gifts[i].split(" ");
    table[dict[give]][dict[gave]] += 1;
    score[dict[give]] -= 1;
    score[dict[gave]] += 1;
  }

  for (let i = 0; i < score.length; i++) {
    let num = 0;
    for (let j = 0; j < score.length; j++) {
      if (i === j) continue;
      if (
        table[j][i] < table[i][j] ||
        (table[j][i] === table[i][j] && score[i] < score[j])
      ) {
        num += 1;
      }
    }
    if (answer < num) answer = num;
  }

  return answer;
}
