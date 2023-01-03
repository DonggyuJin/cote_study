import time

# 모범답안
data = input()

# 시작
start_time = time.time()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
    
print(result)

# 종료
end_time = time.time()
print("time:", end_time-start_time)


"""
# 초기 풀이
# 시작
start_time = time.time()
number = list()

for i in range(0, len(S)):
    number.append(int(S[i]))

number.sort()
result = 1

for i in range(0, len(number)):
    if 0 in number:
        if number[i] == 0:
            continue
        else:
            result = (result * number[i])
    else:
        result = (result * number[i])
    
print(result)
"""