import sys
N=int(input())
D=list(map(int,sys.stdin.readline().split()))
M=max(D)
count=0
for i in range(N):
    count+=(D[i]/M)*100
print(count/N)