import sys
n=int(input())
data=list(map(int,sys.stdin.readline().rstrip().split()))
print(min(data), max(data))