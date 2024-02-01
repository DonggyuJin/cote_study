function solution(n) {
  var answer = 0;

  const dp = Array.from(Array(60001), () => 0);
  dp[0] = 1;
  dp[1] = 2;

  for (let i = 2; i < 60001; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007;
  }

  answer = dp[n - 1];

  return answer;
}
