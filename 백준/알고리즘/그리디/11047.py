import sys
input = sys.stdin.readline

n,k = map(int, input().split())
money = [int(input()) for _ in range(n)]
money.sort(reverse=True)
cnt = 0

for i in money:
  if i > k: continue
  cnt = cnt + (k//i)
  k %= i
print(cnt)