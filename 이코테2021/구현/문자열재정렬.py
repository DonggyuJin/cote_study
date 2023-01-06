import time

# 모범답안
data = input()

# 시작
start_time = time.time()

result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))

# 종료
end_time = time.time()
print("time:", end_time-start_time)

"""
num = '123456789'
data.sort()

for i in range(len(data)):
    if data[i] in num:
        data[i] = int(data[i])
    else:
        continue

count = 0
string = ''

for i in range(len(data)):
    if type(data[i]) == int:
        count += data[i]
    else:
        string += data[i]

print(string + str(count))
"""