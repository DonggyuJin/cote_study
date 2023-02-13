import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
data = Counter(list(map(int, input().split())))
m = int(input())
card = list(map(int, input().split()))

for i in card:
  if i in data: print(data.get(i), end=' ')
  else: print(0, end=' ')