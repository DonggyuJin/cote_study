import sys
input = sys.stdin.readline

n = int(input())
mins = sorted(list(map(int, input().split())))
maxs = sorted(list(map(int, input().split())), reverse=True)

cnt = 0
for i in range(n):
  cnt += mins[i] * maxs[i]
print(cnt)