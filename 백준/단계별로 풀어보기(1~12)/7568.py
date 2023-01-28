import sys
input=sys.stdin.readline
N=int(input())
data=[list(map(int, input().split())) for _ in range(N)]
result=[]

for i in range(N):
    count=0
    for j in range(N):
        if(data[i][0]<data[j][0] and data[i][1]<data[j][1]):
            count+=1
    result.append(count+1)

for i in result: print(i, end=' ')