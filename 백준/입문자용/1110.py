n = input()
count = 0

origin = int(n)
if int(n) < 10:
    n = f'0{n}'
  
while True:
    data = [int(n[:1]), int(n[1:])]
    sum = data[0] + data[1]
    if len(str(sum)) < 2:
        result = n[1:] + str(sum)
    else:
        result = n[1:] + str(sum)[1:]
    n = result
    count += 1
    if origin == int(n):
        break

print(count)