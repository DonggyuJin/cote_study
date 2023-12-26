function solution(s) {
  var answer = "";
  let cnt = 0;

  s.split("").forEach((str) => {
    if (str === " ") {
      cnt = 0;
      answer += " ";
    } else {
      if (cnt === 0 || cnt % 2 === 0) {
        answer += str.toUpperCase();
      } else {
        answer += str.toLowerCase();
      }
      cnt += 1;
    }
  });

  return answer;
}
