import sys
ss=sys.stdin.readline

N=int(ss())
data=[ss().rstrip().split() for _ in range(N)]

data.sort(key=lambda x:int(x[0]))
for i in range(len(data)):print(*data[i])