n = int(input())
n = 1000 - n
count = 0

for coin in [500, 100, 50, 10, 5, 1]:
    count += n//coin
    n %= coin

print(count)

"""
money=[500, 100, 50, 10, 5, 1]
count=0
num=1000-n

for i in range(len(money)):
    if (num // money[i] != 0) and (num % money[i] != 0):
        test = num // money[i]
        num %= money[i]
        count += test
    elif (num // money[i] != 0) and (num % money[i] == 0):
        test = num // money[i]
        count += test
        break
    else: continue

print(count)
"""