import sys
input = sys.stdin.readline

n,m = map(int, input().split())
basket = [0 for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().rstrip().split())
  for i in range(a, b+1):
    basket[i] = c
print(' '.join(map(str, basket[1:])))