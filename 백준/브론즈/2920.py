import sys
origin=[1,2,3,4,5,6,7,8]
data=list(map(int, sys.stdin.readline().split()))
if origin == data: print('ascending')
elif sorted(origin, reverse=True) == data: print('descending')
else: print('mixed')