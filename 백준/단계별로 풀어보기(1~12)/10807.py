import sys
n=int(input())
data=list(map(int,sys.stdin.readline().rstrip().split()))
v=int(input())
print(data.count(v))

"""
count=0
for i in range(len(data)):
    if data[i] == v: count+=1
print(count)
"""