import sys
ss = sys.stdin.readline

data = [int(ss()) for _ in range(5)]
data.sort()

print(sum(data)//5, data[2], sep = '\n')