function solution(s) {
  var answer = 0;

  let result = "";
  const numsObjs = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
  };
  const nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

  let temp = "";
  s.split("").forEach((str) => {
    temp += str;
    if (nums.includes(temp)) {
      result += str;
      temp = "";
    }
    if (numsObjs[temp] !== undefined) {
      result += numsObjs[temp];
      temp = "";
    }
  });

  answer = +result;

  return answer;
}

// function solution(s) {
//     let numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
//     var answer = s;

//     for(let i=0; i< numbers.length; i++) {
//         let arr = answer.split(numbers[i]);
//         answer = arr.join(i);
//     }

//     return Number(answer);
// }
