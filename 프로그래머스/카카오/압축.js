function solution(msg) {
  var answer = [];

  let dict = {};
  for (let i = 1; i <= 26; i++) {
    dict[String.fromCharCode(64 + i)] = i;
  }

  const msgArr = msg.split("");
  let idx = 0;
  let str = "";
  let lastDictNumber = 27;

  while (msgArr.length !== idx) {
    str = str.concat(msgArr[idx]);

    if (dict[str]) idx += 1;
    else {
      answer.push(dict[str.slice(0, str.length - 1)]);
      dict[str] = lastDictNumber;
      lastDictNumber += 1;
      str = "";
    }

    if (msgArr.length === idx) answer.push(dict[str]);
  }

  return answer;
}
