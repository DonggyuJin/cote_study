function solution(record) {
  var answer = [];

  let recordDict = {};
  for (const r of record) {
    const [type, id, name] = r.split(" ");
    if (type === "Enter" || type === "Change") recordDict[id] = name;
  }

  for (const r of record) {
    const [type, id, name] = r.split(" ");
    if (type === "Enter") answer.push(`${recordDict[id]}님이 들어왔습니다.`);
    else if (type === "Leave") answer.push(`${recordDict[id]}님이 나갔습니다.`);
  }

  return answer;
}

// function solution(record) {
//   var answer = [];

//   let recordDict = {};
//   for (const r of record) {
//     const [type, id, name] = r.split(" ");
//     if (type === "Enter" || type === "Change") recordDict[id] = name;
//   }

//   let result = [];
//   for (const r of record) {
//     const [type, id, name] = r.split(" ");
//     if (type === "Enter") result.push(`${id}]님이 들어왔습니다.`);
//     else if (type === "Leave") result.push(`${id}]님이 나갔습니다.`);
//   }

//   for (let i = 0; i < result.length; i++) {
//     const idx = result[i].indexOf("]");
//     const id = result[i].slice(0, idx);
//     const text = result[i].slice(idx);
//     const name = recordDict[id];
//     result[i] = (name + text).replace("]", "");
//   }

//   answer = result;

//   return answer;
// }
