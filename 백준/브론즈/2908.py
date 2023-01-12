import sys
print(max(sys.stdin.readline()[::-1].split()))
"""
a,b=map(str,sys.stdin.readline().split())
ar=a[::-1]
br=b[::-1]
if int(ar) > int(br):
    print(ar)
else:
    print(br)
"""