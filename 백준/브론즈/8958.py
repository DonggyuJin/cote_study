import sys

for _ in range(int(sys.stdin.readline())):
    point = 0
    for x in str(sys.stdin.readline())[:-1].split('X'):
        point += len(x)*(len(x)+1)//2
    print(point)

"""
n=int(input())
data=[]
for _ in range(n):
    p=input()
    data.append(p.split('X'))
for i in range(len(data)):
    count=0
    for j in range(len(data[i])):
        if data[i][j] == "":
            continue
        else:
            count += len(data[i][j])*(len(data[i][j])+1)//2
    print(count)
"""