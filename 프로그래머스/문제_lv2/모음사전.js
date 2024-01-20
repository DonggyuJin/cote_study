const getPermutations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin;
    const permutations = getPermutations(rest, selectNumber - 1);
    const attached = permutations.map((el) => [fixed, ...el]);
    results.push(...attached);
  });

  return results;
};

function solution(word) {
  var answer = 0;

  const words = ["A", "E", "I", "O", "U"];
  let perm = [];
  for (let i = 1; i <= words.length; i++) {
    perm = [...perm, ...getPermutations(words, i).map((el) => el.join(""))];
  }

  perm = perm.sort();
  answer = perm.findIndex((el) => el === word) + 1;

  return answer;
}
