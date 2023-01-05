import time

n = int(input())
x, y = 1, 1
plans = input().split()

# 시작
start_time = time.time()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

# 종료
end_time = time.time()
print("time:", end_time-start_time)

"""
# 초기 풀이
x, y = 1, 1

for i in range(len(data)):
    if((data[i]=='U' and x==1) or (data[i]=='L' and y==1) 
    or (data[i]=='R' and y==n) or (data[i]=='D' and x==n)):
        continue
    if(data[i]=='R'):
        y += 1
    elif(data[i]=='D'):
        x += 1
    elif(data[i]=='L'):
        y -= 1
    elif(data[i]=='U'):
        x -= 1
    
print(x, y)
"""