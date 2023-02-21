import sys
input = sys.stdin.readline

n,m = map(int, input().split())
basket = list(map(int, range(n+1)))
for _ in range(m):
  i,j,k = map(int, input().split())
  basket[i:j+1] = basket[k:j+1] + basket[i:k]
print(' '.join(map(str, basket[1:])))