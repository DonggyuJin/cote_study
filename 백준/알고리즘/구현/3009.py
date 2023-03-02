from collections import Counter
dict1 = []
dict2 = []
for _ in range(3):
  a, b = map(int, input().split())
  dict1.append(a)
  dict2.append(b)

dic1 = Counter(dict1).most_common()
dic2 = Counter(dict2).most_common()

print(dic1[-1][0], dic2[-1][0])

"""
x=[]
y=[]
for i in range(3):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if x.count(x[i]) == 1:
        X = x[i]
    if y.count(y[i]) == 1:
        Y = y[i]
print(X,Y)
"""