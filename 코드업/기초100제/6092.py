n = int(input())
data = list(map(int, input().split()))
a = [0 for _ in range(23)]

for i in range(n):
  for j in range(1, len(a)+1):
    if data[i] == j:
      a[j-1] += 1

for i in range(len(a)):
  print(a[i], end=' ')
