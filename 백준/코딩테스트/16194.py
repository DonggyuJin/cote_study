import sys
input = sys.stdin.readline

n = int(input())
data = [0] + list(map(int, input().split()))
dp = [False for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, i+1):
    if dp[i] == False: dp[i] = dp[i-j]+data[j]
    else: dp[i] = min(dp[i], dp[i-j]+data[j])

print(dp[-1])