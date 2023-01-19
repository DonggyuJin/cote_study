import sys
ss=sys.stdin.readline

N=int(ss())
data=list(map(int,ss().split()))
origin=sorted(list(set(data)))

new={origin[i] : i for i in range(len(origin))}
for i in data:print(new[i], end=' ')
# for i in range(N):print(origin.index(data[i]), end=' ')