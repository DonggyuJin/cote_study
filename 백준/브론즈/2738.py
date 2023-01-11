import sys
n,m=map(int,sys.stdin.readline().strip().split())
A=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
B=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j], end=' ')
    print()