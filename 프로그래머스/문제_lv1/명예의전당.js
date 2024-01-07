function solution(k, score) {
  var answer = [];

  let temp = [];
  for (const num of score) {
    temp.push(num);
    answer.push(
      temp.sort((a, b) => b - a).slice(0, k)[
        temp.length - 1 >= k ? k - 1 : temp.length - 1
      ]
    );
  }

  return answer;
}

// function solution(k, score) {
//     var answer = [];

//     let stack = [];
//     answer = score.reduce((arr, num) =>{
//         if (stack.length < k) {
//             stack.push(num);
//             stack.sort((a, b) => a-b);
//         } else {
//             stack.push(num);
//             stack.sort((a, b) => a-b);
//             stack.shift();
//         }
//         arr.push(stack[0]);
//         return arr;
//     }, []);

//     return answer;
// }
