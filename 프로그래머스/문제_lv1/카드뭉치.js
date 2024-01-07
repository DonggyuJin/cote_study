function solution(cards1, cards2, goal) {
  var answer = "Yes";

  let c1 = 0;
  let c2 = 0;
  for (let i = 0; i < goal.length; i++) {
    if (goal[i] === cards1[c1]) {
      c1 += 1;
      continue;
    }
    if (goal[i] === cards2[c2]) {
      c2 += 1;
      continue;
    }
    return "No";
  }

  return answer;
}
