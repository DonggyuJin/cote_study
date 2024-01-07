const getCombinations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((el) => [fixed, ...el]);
    results.push(...attached);
  });
  return results;
};

function solution(number) {
  var answer = 0;

  const combs = getCombinations(number, 3);
  combs.forEach((comb) => {
    if (comb.reduce((sum, cur) => sum + cur, 0) === 0) {
      answer++;
    }
  });

  return answer;
}
