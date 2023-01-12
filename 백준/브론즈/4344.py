import sys
C=int(input())
for _ in range(C):
    data=list(map(int,sys.stdin.readline().rstrip().split()))
    m=data[0]
    s=sum(data[1:])/m
    count=0
    for i in range(1,m+1):
        if data[i] > s:
            count+=1
    print("{:.3f}%".format(count/(len(data)-1)*100))

"""
import sys
C=int(input())
for _ in range(C):
    data=list(map(int,sys.stdin.readline().rstrip().split()))
    count=0
    for i in range(1,data[0]+1):
        if data[i] > sum(data[1:])/data[0]:
            count+=1
    print("{:.3f}%".format(count/(len(data)-1)*100))
"""
