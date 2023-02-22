import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
cnt = sys.maxsize
idx = 0

for x in range(258):
  maxV, minV = 0, 0

  for i in range(n):
    for j in range(m):
      if land[i][j] >= x:
        maxV += abs(x - land[i][j])
      else:
        minV += abs(x - land[i][j])

  if maxV + b >= minV:
    time = minV + maxV * 2
    if time <= cnt:
      cnt = time
      idx = x

print(cnt, idx)