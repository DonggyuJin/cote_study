data = list(map(int, input().split()))
array = list(map(int, input().split()))
n = data[0]
x = data[1]

for i in range(n):
  if(array[i] < x):
    print(array[i], end=" ")
  else:
    continue
