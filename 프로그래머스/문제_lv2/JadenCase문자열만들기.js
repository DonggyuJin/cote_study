function solution(s) {
  var answer = "";

  let tempS = "";
  let tempG = "";
  let arr = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === " ") {
      if (tempS.length > 0) {
        const newS = arr.push(
          tempS[0].toUpperCase() + tempS.slice(1).toLowerCase()
        );
      }
      tempS = "";
      tempG += " ";
    } else {
      if (tempG.length > 0) {
        arr.push(tempG);
        tempG = "";
      }
      tempS += s[i];
    }
  }

  if (tempS.length > 0) {
    arr.push(tempS[0].toUpperCase() + tempS.slice(1).toLowerCase());
  }
  if (tempG.length > 0) {
    arr.push(tempG);
  }

  answer = arr.join("");

  return answer;
}
