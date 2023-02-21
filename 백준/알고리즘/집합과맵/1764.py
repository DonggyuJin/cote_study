import sys
input = sys.stdin.readline

n,m = map(int, input().split())

dataA = set(input().rstrip() for _ in range(n))
dataB = set(input().rstrip() for _ in range(m))

rs = dataB - (dataB-dataA)
print(len(rs))
print(*sorted(rs), sep='\n')