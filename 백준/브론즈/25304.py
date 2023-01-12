import sys
X=int(input())
N=int(input())
count=0
for _ in range(N):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    count+=a*b
print("Yes" if count==X else "No")