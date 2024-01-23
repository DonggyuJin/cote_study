function solution(cacheSize, cities) {
  var answer = 0;

  if (cacheSize === 0) return 5 * cities.length;

  let stack = [];
  for (const city of cities) {
    const idx = stack.findIndex(
      (el) => el.toLowerCase() === city.toLowerCase()
    );
    if (stack.length !== cacheSize && idx === -1) {
      answer += 5;
      stack.push(city);
      continue;
    }
    if (idx === -1) {
      answer += 5;
      stack.shift();
    } else {
      answer += 1;
      stack = stack.filter((el, index) => index !== idx);
    }
    stack.push(city);
  }

  return answer;
}
