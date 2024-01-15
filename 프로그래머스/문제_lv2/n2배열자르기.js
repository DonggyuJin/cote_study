function solution(n, left, right) {
  var answer = [];

  // let arr = Array.from(Array(n), () => new Array(n).fill(0));

  // for(let i=0; i<arr.length; i++){
  //     for(let j=0; j<arr[0].length; j++){
  //         const num = Math.max(i, j);
  //         arr[i][j] = num+1;
  //     }
  // }

  // let newArr = [];
  // for(const el of arr){
  //     newArr = [...newArr, ...el];
  // }

  // answer = newArr.slice(left, right+1);

  for (let i = left; i <= right; i++) {
    const div = Math.floor(i / n);
    const rest = i % n;

    if (div >= rest) answer.push(div + 1);
    else answer.push(rest + 1);
  }

  return answer;
}
