import sys
input = sys.stdin.readline

n=int(input())

for _ in range(n):
    ps = input().rstrip()
    while '()' in ps:
        ps = ps.replace('()', '')
    if ps == '': print("YES")
    else: print("NO")