function solution(s) {
  var answer = 0;

  let x = "";
  let temp = "";

  for (let i = 0; i < s.length; i++) {
    if (x.length === temp.length) {
      answer += 1;
      x = "";
      temp = "";
    }

    if (x === "" || s[i] === x[0]) {
      x += s[i];
    } else {
      temp += s[i];
    }
  }

  return answer;
}
