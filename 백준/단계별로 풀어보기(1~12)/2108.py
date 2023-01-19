import sys
from collections import Counter
ss=sys.stdin.readline

N=int(ss())
data=[int(ss()) for _ in range(N)]

print(round(sum(data)/N))

data.sort()
print(data[int(N/2)])

many=Counter(data).most_common()
if len(many) > 1:
    if many[0][1] == many[1][1]:print(many[1][0])
    else:print(many[0][0])
else:print(many[0][0])

print(data[-1]-data[0])