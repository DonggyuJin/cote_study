import sys
ss = sys.stdin.readline

N=int(ss())
data=sorted([int(ss()) for _ in range(N)])
# data.sort()

print(*data, sep='\n')