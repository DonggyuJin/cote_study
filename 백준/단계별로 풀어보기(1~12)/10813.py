import sys
input = sys.stdin.readline

n,m = map(int, input().split())
basket = list(map(int, range(n+1)))
for _ in range(m):
  a, b = map(int, input().rstrip().split())
  temp = basket[b]
  basket[b] = basket[a]
  basket[a] = temp
print(' '.join(map(str, basket[1:])))