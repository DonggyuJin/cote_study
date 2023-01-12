R=range(1,10001)
D=set(R)
S=set()
for i in R:
    for j in str(i):
        i += int(j)
    S.add(i)
result=sorted(D-S)
for i in result: print(i)