function solution(elements) {
  var answer = 0;

  let results = [];
  const newArr = [...elements, ...elements];

  elements.forEach((element, idx) => {
    if (idx < elements.length) {
      for (let i = 0; i < elements.length; i++) {
        const arr = newArr.slice(i, i + 1 + idx);
        results.push(arr.reduce((acc, val) => acc + val, 0));
      }
    }
  });

  const set = new Set(results);
  answer = [...set].length;

  return answer;
}
