from itertools import permutations

n,m=map(int, input().split())
data = list(permutations([i for i in range(1, n+1)], m))

for i in range(len(data)): print(*data[i])