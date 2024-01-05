function solution(survey, choices) {
  var answer = "";

  const score = { 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3 };
  let type = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 };

  for (let i = 0; i < survey.length; i++) {
    let [fir, sec] = survey[i].split("");
    const choice = choices[i];
    if (choice === 4) continue;
    if (choice < 4) type[fir] += score[choice];
    else if (choice > 4) type[sec] += score[choice];
  }

  for (let i = 0; i < 7; i += 2) {
    const temp = Object.entries(type).slice(i, i + 2);
    if (temp[0][1] === temp[1][1]) answer += temp[0][0];
    if (temp[0][1] > temp[1][1]) answer += temp[0][0];
    else if (temp[0][1] < temp[1][1]) answer += temp[1][0];
  }

  return answer;
}

// JS 참고
// function solution(survey, choices) {
//     const MBTI = {};
//     const types = ["RT","CF","JM","AN"];

//     types.forEach((type) =>
//         type.split('').forEach((char) => MBTI[char] = 0)
//     )

//     choices.forEach((choice, index) => {
//         const [disagree, agree] = survey[index];

//         MBTI[choice > 4 ? agree : disagree] += Math.abs(choice - 4);
//     });

//     return types.map(([a, b]) => MBTI[b] > MBTI[a] ? b : a).join("");
// }
