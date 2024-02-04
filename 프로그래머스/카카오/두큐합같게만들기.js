function solution(queue1, queue2) {
  var answer = 0;

  const queue = [...queue1, ...queue2];
  const max = queue.length * 3;
  const target = queue.reduce((sum, cur) => sum + cur, 0) / 2;

  let start = 0;
  let end = queue1.length;
  let totalSum = queue.slice(start, end).reduce((sum, cur) => sum + cur, 0);

  while (answer <= max) {
    if (target > totalSum) {
      totalSum += queue[end];
      end += 1;
    } else if (target < totalSum) {
      totalSum -= queue[start];
      start += 1;
    } else if (target === totalSum) return answer;
    answer += 1;
  }

  return -1;
}

// function solution(queue1, queue2) {
//     var answer = 0;

//     const divide = parseInt([...queue1, ...queue2].reduce((sum, cur) => sum + cur, 0) / 2);
//     while(true){
//         const sum1 = queue1.reduce((sum, cur) => sum + cur, 0);
//         const sum2 = queue2.reduce((sum, cur) => sum + cur, 0);
//         if(sum1 === divide && sum2 === divide) break;
//         if(sum1 === 0 || sum2 === 0) return -1;

//         if(sum1 < sum2){
//             const shift = queue2.shift();
//             queue1.push(shift);
//         } else {
//             const shift = queue1.shift();
//             queue2.push(shift);
//         }

//         answer += 1;
//     }

//     console.log(queue1, queue2);

//     return answer;
// }

// class Queue {
//     constructor(){
//         this.storage = {};
//         this.front = 0;
//         this.rear = 0;
//     }

//     size() {
//         if(this.storage[this.rear] === undefined) return 0;
//         else return this.rear - this.rear + 1;
//     }

//     append(value) {
//         if(this.size() === 0){
//             this.storage['0'] = value;
//         } else {
//             this.rear += 1;
//             this.storage[this.rear] = value;
//         }
//     }

//     popleft() {
//         let temp;
//         temp = this.storage[this.front];
//         delete this.storage[this.front];
//         if(this.front === this.rear){
//             this.front = 0;
//             this.rear = 0;
//         } else {
//             this.front += 1;
//         }
//         return temp;
//     }

//     sum() {
//         return Object.values(this.storage).reduce((sum, cur) => sum + cur, 0);
//     }
// }

// function solution(queue1, queue2) {
//     var answer = 0;

//     const queue = [...queue1, ...queue2];
//     const divide = parseInt(queue.reduce((sum, cur) => sum + cur, 0) / 2);

//     const q1 = new Queue();
//     const q2 = new Queue();

//     for(let i=0; i<queue1.length; i++){
//         q1.append(queue1[i]);
//         q2.append(queue2[i]);
//     }

//     console.log(q1.sum(), q2.sum());

//     while(true){
//         const sum1 = q1.sum();
//         const sum2 = q2.sum();
//         if(sum1 === divide && sum2 === divide) break;
//         if(sum1 === 0 || sum2 === 0) return -1;

//         if(sum1 < sum2){
//             const shift = q2.popleft();
//             q1.append(shift);
//         } else {
//             const shift = q1.popleft();
//             q2.append(shift);
//         }

//         answer += 1;
//     }

//     return answer;
// }
