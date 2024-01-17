function solution(clothes) {
  var answer = 1;

  let cloSet = {};
  for (const clo of clothes) {
    if (cloSet[clo[1]]) cloSet[clo[1]] += 1;
    else cloSet[clo[1]] = 1;
  }

  for (const val of Object.values(cloSet)) {
    answer *= val + 1;
  }

  answer -= 1;

  return answer;
}
