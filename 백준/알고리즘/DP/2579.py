import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
dp = [0] * (n)
if len(num) <= 2: print(sum(num))
else:
  dp[0] = num[0]
  dp[1] = max(num[0]+num[1], num[1])
  dp[2] = max(num[1]+num[2], num[0]+num[2])
  for i in range(3, n):
    dp[i] = max(dp[i-3]+num[i-1], dp[i-2]) + num[i]
  print(dp[-1])