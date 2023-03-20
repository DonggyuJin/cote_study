import sys, operator
input = sys.stdin.readline

n = int(input())
dict = {}
for _ in range(n):
  a,b,c,d = map(str, input().rstrip().split())
  dict[a] = int(d+c.zfill(2)+b.zfill(2))
dict = sorted(dict.items(), key=operator.itemgetter(1))

print(dict[-1][0])
print(dict[0][0])