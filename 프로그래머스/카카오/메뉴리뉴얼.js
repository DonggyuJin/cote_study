const getCombinations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((el) => [fixed, ...el].sort());
    results.push(...attached);
  });

  return results;
};

function solution(orders, course) {
  var answer = [];

  let orderDict = {};
  for (const order of orders) {
    orderDict[order] = [];
  }
  for (const order of orders) {
    const orderArr = order.split("");
    for (let i = 2; i <= orderArr.length; i++) {
      orderDict[order].push(...getCombinations(orderArr, i));
    }
  }

  let newDict = {};
  for (const [key, val] of Object.entries(orderDict)) {
    for (const v of val) {
      if (newDict[v.join("")]) newDict[v.join("")] += 1;
      else newDict[v.join("")] = 1;
    }
  }

  newDict = Object.fromEntries(
    Object.entries(newDict).sort(([x, a], [y, b]) => b - a)
  );

  let temp = {};
  for (const [key, val] of Object.entries(newDict)) {
    if (temp[key.length]) {
      if (val >= temp[key.length]) {
        if (course.includes(key.length)) answer.push(key);
      }
    } else {
      if (val > 1) {
        if (course.includes(key.length)) answer.push(key);
        temp[key.length] = val;
      }
    }
  }

  answer = answer.sort();

  return answer;
}
