function solution(fees, records) {
  var answer = [];

  for (let i = 0; i < records.length; i++) {
    const newRecords = records[i].split(" ");
    const [h, m] = newRecords[0].split(":");
    const minute = +h * 60 + +m;
    records[i] = newRecords;
    newRecords[0] = minute;
  }

  let inDict = {};
  let outDict = {};
  for (const record of records) {
    const [time, carNum, type] = record;
    if (type === "IN") {
      inDict[carNum] = time;
      if (time === 0) inDict[carNum] = -1;
    } else {
      if (outDict[carNum]) outDict[carNum] += time - inDict[carNum];
      else outDict[carNum] = time - inDict[carNum];
      inDict[carNum] = 0;
    }
  }

  for (const [key, val] of Object.entries(inDict)) {
    if (val === -1) outDict[key] = 23 * 60 + 59;
    else if (val !== 0) {
      if (outDict[key]) outDict[key] += 23 * 60 + 59 - val;
      else outDict[key] = 23 * 60 + 59 - val;
    }
  }

  const [bt, bp, ut, up] = fees;
  const result = Object.keys(outDict).sort();
  for (const res of result) {
    if (outDict[res] >= bt)
      answer.push(bp + Math.ceil((outDict[res] - bt) / ut) * up);
    else answer.push(bp);
  }

  return answer;
}
