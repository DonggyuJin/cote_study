function solution(name, yearning, photo) {
  var answer = [];

  let nameObj = {};
  for (let i = 0; i < name.length; i++) {
    nameObj[name[i]] = yearning[i];
  }

  for (const p of photo) {
    let temp = 0;
    for (const n of p) {
      if (nameObj[n]) {
        temp += nameObj[n];
      }
    }
    answer.push(temp);
  }

  return answer;
}
