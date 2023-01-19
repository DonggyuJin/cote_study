import sys
n=int(input())
for _ in range(n):
    a,b=map(str, sys.stdin.readline().split())
    for i in range(len(b)):
        print(b[i]*int(a), end='')
    print()