N=int(input())
L,E=0,0
while N>E:
    L+=1
    E+=L
result=E-N
if L%2==0:
    left=L-result
    right=result+1
else:
    left=result+1
    right=L-result
print(f'{left}/{right}')