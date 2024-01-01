function solution(babbling) {
  let answer = 0;
  let comb = ["aya", "ye", "woo", "ma"];

  for (let i = 0; i < babbling.length; i++) {
    for (let j = 0; j < comb.length; j++) {
      if (babbling[i].includes(comb[j].repeat(2))) {
        break;
      }
      babbling[i] = babbling[i].split(comb[j]).join("!");
    }
  }

  answer = babbling.filter((e) => {
    return /(^!+$)/.test(e);
  }).length;

  return answer;
}
