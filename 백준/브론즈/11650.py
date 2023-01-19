import sys
N=int(sys.stdin.readline())
x,y=[],[]

for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

for i in range(N):
    print(x[i],y[i])