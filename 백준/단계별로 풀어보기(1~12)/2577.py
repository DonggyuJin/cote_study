A=int(input())
B=int(input())
C=int(input())
r=A*B*C
d=list(str(r))
for i in range(10):
    print(d.count(str(i)))