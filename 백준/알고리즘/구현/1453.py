import sys
input = sys.stdin.readline

n = int(input())
rs = list(map(int, input().split()))
new_rs = set(rs)
print(len(rs) - len(new_rs))