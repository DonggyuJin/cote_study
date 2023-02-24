import sys
input = sys.stdin.readline

k,n = map(int, input().split())
l = [int(input()) for _ in range(k)]

start = 1
end = max(l)

while start <= end:
  mid = (start + end) // 2
  cnt = 0
  
  for i in l:
    cnt += i // mid

  if cnt >= n:
    start = mid + 1
  elif cnt < n:
    end = mid - 1

print(end)