N=int(input())
for i in range(2,int(N**(0.5))+2):
    while N%i==0:
        print(i)
        N//=i
if N!=1: print(N)

"""
N=int(input())
S=2
while N>1:
    if N%S==0:
        N/=S
        print(S)
        continue
    S+=1
"""