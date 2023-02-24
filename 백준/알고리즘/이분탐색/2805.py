import sys
input = sys.stdin.readline

k,n = map(int, input().split())
l = list(map(int, input().split()))

start = 1
end = max(l)

maxV = 0
while start <= end:
  mid = (start + end) // 2
  cnt = 0
  
  for i in l:
    if i > mid:
      cnt += i - mid

  if cnt >= n:
    start = mid + 1
    maxV = max(maxV, mid)
  elif cnt < n:
    end = mid - 1

print(maxV)