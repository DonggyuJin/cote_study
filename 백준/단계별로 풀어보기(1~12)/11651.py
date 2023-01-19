import sys
N=int(sys.stdin.readline())
data=[]

for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    data.append([a,b])

data.sort(key=lambda x:(x[1], x[0]))

for i in data:
    print(i[0], i[1])