import sys
T=int(input())
for _ in range(T):
    h,w,n=map(int, sys.stdin.readline().split())
    y=n%h
    x=n//h
    
    if y==0:
        if len(str(x))==1:print(f'{h}0{x}')
        else:print(f'{h}{x}')
    elif len(str(x+1))==1:print(f'{y}0{x+1}')
    else:print(f'{y}{x+1}')

"""
for _ in range(T):
    count=0
    x,y=1,1
    h,w,n=map(int, sys.stdin.readline().split())
    while count<n:
        if y<h:
            y+=1
        elif y==h:
            x+=1
            y=1
        count+=1
    if len(str(x))==1:print(f'{y-1}0{x}')
    else:print(f'{y-1}{x}')
"""

"""
for _ in range(T):
    h,w,n=map(int, sys.stdin.readline().split())
    hotel=[[(i+1)*100+(j+1) for j in range(w)] for i in range(h)]
    while count<n:
        if y<h:
            y+=1
        elif y==h:
            y=0
            x+=1
        count+=1
    print(hotel[y][x])
"""