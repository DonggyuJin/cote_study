function recur(p, idx) {
  let str = "";
  let cnt = 0;
  let flag = false;

  for (let i = idx; i < p.length; i++) {
    p[i] === "(" ? cnt++ : cnt--;
    cnt < 0 ? (flag = true) : 0;
    str += p[i];
    if (cnt === 0) {
      idx = i + 1;
      break;
    }
  }

  if (flag) {
    str = str.slice(1, -1);
    let temp = "";
    for (const e of str) {
      e === "(" ? (temp += ")") : (temp += "(");
    }
    str = temp;
    if (p.length === idx) return "()" + str;
    return "(" + recur(p, idx) + ")" + str;
  } else {
    if (p.length === idx) return str;
    return str + recur(p, idx);
  }
}

function solution(p) {
  var answer = recur(p, 0);

  return answer;
}
