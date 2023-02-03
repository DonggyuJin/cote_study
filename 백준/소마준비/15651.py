import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())
# data = list(product([i for i in range(1, n+1)], repeat=m))

# for i in range(len(data)): print(*data[i])

data = map(str, range(1, n+1))
print('\n'.join(map(' '.join, product(data, repeat=m))))