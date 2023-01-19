from sys import stdin as ss
while True:
    data=list(map(int,ss.readline().split()))
    if data[0]==0 and data[1]==0 and data[2]==0:
        break
    data.sort()
    if data[2]*data[2] == (data[0]*data[0]+data[1]*data[1]):print('right')
    else:print('wrong')