import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    text = list(input().split())
    for i in range(len(text)):
        print(text[i][::-1], end=' ')