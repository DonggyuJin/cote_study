function solution(today, terms, privacies) {
  var answer = [];

  let termObj = {};
  for (const term of terms) {
    const [type, month] = term.split(" ");
    termObj[type] = +month;
  }

  for (let i = 0; i < privacies.length; i++) {
    let [date, type] = privacies[i].split(" ");
    date = new Date(date);
    date = new Date(date.setMonth(date.getMonth() + termObj[type]));

    if (new Date(today).getTime() >= date.getTime()) {
      answer.push(i + 1);
    }
  }

  return answer;
}

// 참고
// function solution(today, terms, privacies) {
//     var answer = [];
//     var [year, month, date] = today.split(".").map(Number);
//     var todates = year * 12 * 28 + month * 28 + date;
//     var t = {};
//     terms.forEach((e) => {
//       let [a, b] = e.split(" ");
//       t[a] = Number(b);
//     });
//     privacies.forEach((e, i) => {
//       var [day, term] = e.split(" ");
//       day = day.split(".").map(Number);
//       var dates = day[0] * 12 * 28 + day[1] * 28 + day[2] + t[term] * 28;
//       if (dates <= todates) answer.push(i + 1);
//     });
//     return answer;
//   }
