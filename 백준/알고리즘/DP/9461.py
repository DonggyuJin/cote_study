import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  dp = [1, 1, 1, 2, 2]
  for k in range(5, 101):
    dp.append(dp[k-1]+dp[k-5])
  print(dp[n-1])