import sys
input = sys.stdin.readline

n = int(input())
rs = [int(input()) for _ in range(n)]
if rs.count(1) > rs.count(0): print("Junhee is cute!")
else: print("Junhee is not cute!")