import sys
data=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
new_data=[]
for i in range(9):    
    new_data.append(max(data[i]))
num=max(new_data)
for i in range(9):
    if num in data[i]:
        print(num)
        print(i+1, data[i].index(num)+1)
    else:
        pass