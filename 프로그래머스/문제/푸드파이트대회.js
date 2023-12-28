function solution(food) {
  var answer = "";

  let temp = "";
  food.map((f, idx) => {
    if (idx === 0) return;
    answer += idx.toString().repeat(parseInt(f / 2));
  });

  temp = answer.split("").reverse().join("");
  answer = answer + "0" + temp;

  return answer;
}
