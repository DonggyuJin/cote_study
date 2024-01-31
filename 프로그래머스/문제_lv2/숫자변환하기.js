function solution(x, y, n) {
  var answer = 0;

  let dp = Array.from(Array(1000001), () => -1);
  dp[x] = 0;

  for (let i = x; i <= y; i++) {
    if (dp[i] !== -1) {
      if (i + n <= y) {
        if (dp[i + n] === -1) dp[i + n] = dp[i] + 1;
        else if (dp[i + n] !== -1) dp[i + n] = Math.min(dp[i] + 1, dp[i + n]);
      }
      if (i * 2 <= y) {
        if (dp[i * 2] === -1) dp[i * 2] = dp[i] + 1;
        else if (dp[i * 2] !== -1) dp[i * 2] = Math.min(dp[i] + 1, dp[i * 2]);
      }
      if (i * 3 <= y) {
        if (dp[i * 3] === -1) dp[i * 3] = dp[i] + 1;
        else if (dp[i * 3] !== -1) dp[i * 3] = Math.min(dp[i] + 1, dp[i * 3]);
      }
    }
  }

  answer = dp[y];

  return answer;
}
