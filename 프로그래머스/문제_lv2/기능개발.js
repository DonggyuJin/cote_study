function solution(progresses, speeds) {
  var answer = [];

  let deploy = [];
  for (let i = 0; i < progresses.length; i++) {
    const num = 100 - progresses[i];
    const div = parseInt(num / speeds[i]);
    const rest = num % speeds[i];
    if (rest === 0) deploy.push(div);
    else deploy.push(div + 1);
  }

  let temp = deploy[0];
  let wait = 1;
  for (let i = 1; i < deploy.length; i++) {
    if (temp >= deploy[i]) wait += 1;
    else if (temp < deploy[i]) {
      answer.push(wait);
      wait = 1;
    }
    temp = Math.max(temp, deploy[i]);
  }

  answer.push(wait);

  return answer;
}
