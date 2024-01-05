function solution(N, stages) {
  var answer = [];

  let users = stages.length;
  let stageObj = {};

  for (let i = 1; i <= N + 1; i++) {
    stageObj[i] = 0;
  }

  for (const stage of stages) {
    stageObj[stage] += 1;
  }

  for (let i = 1; i < N + 1; i++) {
    let fail = stageObj[i] / users;
    users -= stageObj[i];
    stageObj[i] = fail;
  }

  const newArr = Object.entries(stageObj).sort((a, b) => b[1] - a[1]);
  for (const el of newArr) {
    let num = +el[0];
    if (num > N) continue;
    answer.push(num);
  }

  return answer;
}
