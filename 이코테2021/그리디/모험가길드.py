import time

# 모범답안
n = int(input())
data = list(map(int, input().split))
data.sort()

# 시작
start_time = time.time()
result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result +=1
        count = 0

print(result)

# 종료
end_time = time.time()
print("time:", end_time-start_time)

"""
# 초기 풀이
result = 0

X.sort()

print(X)

for i in range(1, N):
    print(i)
    if X[i-1] >= X[i]:
        result += 1
    
print(result)
"""