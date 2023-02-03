import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
data = map(str, range(1, n+1))

print('\n'.join(map(' '.join, combinations_with_replacement(data, m))))