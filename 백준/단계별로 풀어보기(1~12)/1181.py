import sys
ss=sys.stdin.readline

N=int(ss())
data=sorted(list(set([ss().rstrip() for _ in range(N)])))

data.sort(key=len)
print(*data, sep='\n')