function solution(s) {
  var answer = [];

  let num = 0;
  let cnt = 0;
  while (+s !== 1) {
    num += 1;

    s.split("").map((str) => {
      if (str === "0") cnt += 1;
    });

    s = s.replaceAll("0", "");
    s = s.length.toString(2);
  }

  answer = [num, cnt];

  return answer;
}
