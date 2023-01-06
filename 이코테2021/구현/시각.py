import time

# 모범답안
h = int(input())
count = 0

# 시작
start_time = time.time()

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 종료
end_time = time.time()
print("time:", end_time-start_time)

"""
for i in range(0, n+1):
    for j in range(0, 60):
        for k in range(0, 60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                result += 1

print(result)
"""