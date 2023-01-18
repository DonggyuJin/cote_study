import sys
ss = sys.stdin.readline

N,k=map(int, ss().split())
score=sorted(list(map(int, ss().split())))

print(score[-k])
