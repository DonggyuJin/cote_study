import sys
d=list(map(int,sys.stdin.readline().rstrip().split()))
p=[1,1,2,2,2,8]
for i in range(len(d)):
    print(p[i]-d[i], end=' ')

"""
import sys
d=list(map(int,sys.stdin.readline().rstrip().split()))
p=[1,1,2,2,2,8]
for i in range(len(d)):
    if d[i]>p[i] or d[i]<p[i]:
        print(p[i]-d[i], end=' ')
    else:
        print(0, end=' ')
"""