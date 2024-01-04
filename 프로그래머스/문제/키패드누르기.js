function solution(numbers, hand) {
  var answer = "";

  function keypadPos(key) {
    const keypad = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      ["*", 0, "#"],
    ];
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 3; j++) {
        if (keypad[i][j] === key) {
          return [i, j];
        }
      }
    }
  }

  let l = "*";
  let r = "#";

  for (const num of numbers) {
    if (num === 1 || num === 4 || num === 7) {
      answer += "L";
      l = num;
    } else if (num === 3 || num === 6 || num === 9) {
      answer += "R";
      r = num - 2;
    } else {
      const ll = keypadPos(l);
      const rr = keypadPos(r);
      const m = keypadPos(num);

      const ld = Math.abs(ll[0] - m[0]) + Math.abs(ll[1] - m[1]);
      const rd = Math.abs(rr[0] - m[0]) + Math.abs(rr[1] - m[1]);

      if (rd === ld) {
        hand === "right"
          ? ((r = num), (answer += "R"))
          : ((l = num), (answer += "L"));
      } else if (rd > ld) {
        answer += "L";
        l = num;
      } else {
        answer += "R";
        r = num;
      }
    }
  }

  return answer;
}
