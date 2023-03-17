import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

if a*len(b) == b*len(a): print(1)
else: print(0)