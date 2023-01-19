import sys
h,m=map(int,sys.stdin.readline().rstrip().split())
cook=int(input())
sums=h*60+m+cook
H=sums//60
M=sums%60
print(H if H<24 else H%24, M)