import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

num.sort()
cnt = 0
for i in range(n+1):
  cnt += sum(num[:i])
print(cnt)