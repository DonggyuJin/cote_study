from sys import stdin as ss
a,b,c=map(int,ss.readline().split())
print(-1 if b>=c else (a//(c-b))+1)