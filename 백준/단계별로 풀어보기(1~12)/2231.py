import sys
input=sys.stdin.readline

N=input().rstrip()
X=int(N)//2
result=0

while X < int(N):
    num=list(map(int, str(X)))
    if(X+sum(num)==int(N)):
        result=X
        break
    else: X+=1

print(result)

"""
N = int(input())
result = 0
for i in range(max(0,N-len(str(N))*9),N):
    if sum(map(int,str(i))) + i == N:
        result = i
        break
print(result)
"""