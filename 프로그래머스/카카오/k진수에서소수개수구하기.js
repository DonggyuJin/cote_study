const isPrime = (num) => {
  if (num === 0 || num === 1) return false;

  for (let i = 2; i <= +Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }

  return true;
};

function solution(n, k) {
  var answer = 0;

  const resArr = n.toString(k).split("0");
  answer = resArr.filter((res) => isPrime(+res)).length;

  return answer;
}
