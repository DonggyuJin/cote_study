function solution(people, limit) {
  var answer = 0;

  people = people.sort((a, b) => a - b);
  let lt = 0;
  let rt = people.length - 1;

  while (lt <= rt) {
    let sum = people[lt] + people[rt];
    if (lt != rt-- && sum <= limit) {
      lt += 1;
    }
    answer += 1;
  }

  return answer;
}
