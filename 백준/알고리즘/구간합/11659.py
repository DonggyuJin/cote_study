import sys
input = sys.stdin.readline

n,m = map(int, input().split())
data = list(map(int, input().split()))
for i in range(n-1):
  data[i+1] += data[i]
data = [0] + data

for _ in range(m):
  a, b = map(int, input().split())
  print(data[b]-data[a-1])