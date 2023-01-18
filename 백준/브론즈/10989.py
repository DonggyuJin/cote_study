import sys
ss = sys.stdin.readline

N=int(ss())
data=[0]*10000

for i in range(N):
    num=int(ss())
    data[num-1]=data[num-1]+1

for i in range(10000):
    if data[i]!=0:
        for j in range(data[i]):
            print(i+1)
