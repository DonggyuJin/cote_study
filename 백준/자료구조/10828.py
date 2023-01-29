import sys
input = sys.stdin.readline

n=int(input())
data=[]

for _ in range(n):
    a=input()
    if 'push' in a:
        a = list(a.split())
        data.append(a[1])
    elif 'pop' in a:
        if len(data) > 0:
            print(data[-1])
            data.pop(-1)
        else: print(-1)
    elif 'size' in a:
        print(len(data))
    elif 'empty' in a:
        if len(data) > 0: print(0)
        else: print(1)
    elif 'top' in a:
        if len(data) > 0: print(data[-1])
        else: print(-1)