import sys
I=sys.stdin.readline

M=int(I())
N=int(I())
data=[]

for i in range(M, N+1):
    data.append(i)
    for j in range(2,int(i**1/2)+1):
        if i%j==0:
            data.remove(i)
            break

if 1 in data:data.remove(1)

if data==[]:print(-1)
else:print(sum(data), min(data), sep='\n')