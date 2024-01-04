function solution(ingredient) {
  var answer = 0;

  let temp = [];
  for (let i = 0; i < ingredient.length; i++) {
    temp.push(ingredient[i]);
    const l = temp.length;
    if (l >= 4) {
      if (
        temp[l - 1] === 1 &&
        temp[l - 2] === 3 &&
        temp[l - 3] === 2 &&
        temp[l - 4] === 1
      ) {
        answer += 1;
        temp.pop();
        temp.pop();
        temp.pop();
        temp.pop();
      }
    }
  }

  return answer;
}
