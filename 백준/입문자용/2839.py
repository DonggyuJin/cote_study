n = int(input())
count = 0

if n % 5 == 0:
  count += n // 5
else:
  while n > 0:
    n = n - 3
    count = count + 1
    if n % 5 == 0:
      count += n // 5
      break
    elif n == 1 or n == 2:
      count = -1
      break
    elif n == 0:
      break
  
print(count)