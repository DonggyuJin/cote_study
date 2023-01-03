import time

N, K = map(int, input().split())

# 시작
start_time = time.time()
# 모범답안
count = 0

while True:
    target = (N // K) * K
    count += (N - target)
    N = target

    if N < K:
        break
    
    count += 1
    N //= K

count += (N - 1)
print(count)
# 종료
end_time = time.time()
print("time:", end_time-start_time)

"""
# 처음 생각한 풀이
count = 0

while N > 1:
    if N % K == 0:
        N /= K
        count +=1
    else:
        N -= 1
        count +=1

print(count)
"""