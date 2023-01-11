import sys
t=int(input())
while t>0:
    a,b=map(int,sys.stdin.readline().rstrip().split())
    print(a+b)
    t-=1