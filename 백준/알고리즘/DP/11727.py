import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1, 3]
for k in range(3, n+1):
  dp.append((dp[k-2]*2) + dp[k-1])
print(dp[n]%10007)