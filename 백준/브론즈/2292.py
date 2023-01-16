N=int(input())
a=2
if N==1:print(1)
for i in range(0, N): 
    s=a+(i)*6
    if s <= N < s+(i+1)*6:
        print(i+2)
        break
    a=s