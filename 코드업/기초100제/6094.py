n = int(input())
data = list(map(int, input().split()))

print(min(data))

"""
# 소스 2번
n = int(input())
data = list(map(int, input().split()))

for i in range(n):
  for j in range(1, n):
    temp = 0
    if data[j-1] > data[j]:
      temp = data[j]
      data[j] = data[j-1]
      data[j-1] = temp
    else:
      continue

print(data[0])
"""

"""
# 소스 3번
n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

result = a[0]
for i in range(0, n) :
  if a[i] < result :
    result = a[i]

print(result)

"""