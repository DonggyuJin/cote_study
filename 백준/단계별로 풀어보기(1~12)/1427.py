from sys import stdin as ss
N=sorted(list(map(int, ss.readline().rstrip())), reverse=True)
print(*N,sep='')