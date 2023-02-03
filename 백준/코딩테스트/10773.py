import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    a = int(input())
    if a != 0: data.append(a)
    elif a == 0: data.pop()

print(sum(data))
