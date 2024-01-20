const getPermutations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = getPermutations(rest, selectNumber - 1);
    const attached = permutations.map((el) => [fixed, ...el]);
    results.push(...attached);
  });

  return results;
};

function solution(k, dungeons) {
  var answer = -1;

  let temp;
  let result;
  const dunArr = getPermutations(dungeons, dungeons.length);
  for (let i = 0; i < dunArr.length; i++) {
    temp = k;
    result = 0;
    for (let j = 0; j < dunArr[i].length; j++) {
      if (temp >= dunArr[i][j][0]) {
        result += 1;
        temp -= dunArr[i][j][1];
      }
    }
    answer = Math.max(answer, result);
  }

  return answer;
}
