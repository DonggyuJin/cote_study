function solution(dartResult) {
  let num = 0;
  let tmp = [];

  for (let i = 0; i < dartResult.length; i++) {
    if (!isNaN(dartResult[i])) {
      num = Number(dartResult[i - 1]) === 1 ? 10 : Number(dartResult[i]);
    }
    let len = tmp.length;
    if (dartResult[i] === "S") tmp.push(num);
    if (dartResult[i] === "D") tmp.push(num ** 2);
    if (dartResult[i] === "T") tmp.push(num ** 3);
    if (dartResult[i] === "*") {
      tmp[len - 2] *= 2;
      tmp[len - 1] *= 2;
    }
    if (dartResult[i] === "#") tmp[len - 1] *= -1;
  }

  return tmp.reduce((a, b) => a + b, 0);
}

// function solution(dartResult) {
//   const bonus = { 'S': 1, 'D': 2, 'T': 3 },
//         options = { '*': 2, '#': -1, undefined: 1 };

//   let darts = dartResult.match(/\d.?\D/g);

//   for (let i = 0; i < darts.length; i++) {
//       let split = darts[i].match(/(^\d{1,})(S|D|T)(\*|#)?/),
//           score = Math.pow(split[1], bonus[split[2]]) * options[split[3]];

//       if (split[3] === '*' && darts[i - 1]) darts[i - 1] *= options['*'];

//       darts[i] = score;
//   }

//   return darts.reduce((a, b) => a + b);
// }
