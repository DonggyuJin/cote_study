function solution(id_list, report, k) {
  var answer = [];

  let myReport = {};
  let resReport = {};
  for (const id of id_list) {
    myReport[id] = 0;
    resReport[id] = 0;
  }

  let setReport = [...new Set(report)];
  for (const report of setReport) {
    const [reporter, receiver] = report.split(" ");
    myReport[receiver] += 1;
  }

  for (const report of setReport) {
    const [reporter, receiver] = report.split(" ");
    if (myReport[receiver] >= k) {
      resReport[reporter] += 1;
    }
  }

  answer = Object.values(resReport);

  return answer;
}
