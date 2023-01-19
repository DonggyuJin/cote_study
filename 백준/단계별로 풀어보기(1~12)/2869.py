import sys,math
a,b,v=map(int, sys.stdin.readline().split())
print(math.ceil((v-b)/(a-b)))

"""
if a==v:print(1)
elif a-b==1 and b==v:print(v-b+1)
elif a-b==1 and a!=v:print(v-b)
elif a>=v:print((a//v)+1)
elif v%a==0 or b==1:print((v//(a-b))+1)
else:print(v//(a-b))
"""

"""
x,y,z=0,0,0
count=0
while True:
    count+=1
    if a-b==1:
        print(v-b)
    if y+b>=v:
        print(count)
        break
    y=x+a
    z=y-b
    x=z
"""    