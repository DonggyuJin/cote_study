import sys
input = sys.stdin.readline

maxV = 0
for _ in range(int(input())):
  rs = list(map(int, input().split()))
  rs.sort()
  
  if len(set(rs)) == 1:
    money = 50000 + (rs[0] * 5000)
      
  elif len(set(rs)) == 2:
    if rs[1] == rs[2]:
      money = 10000 + (rs[1] * 1000)
    elif rs[1] != rs[2]:
      money = 2000 + (rs[0] * 500) + (rs[2] * 500)
  elif len(set(rs)) == 3:
    for i in range(3):
      if rs[i] == rs[i+1]:
        money = 1000 + (rs[i] * 100)
        break
  else:
    money = max(rs) * 100
  
  if money > maxV:
    maxV = money

print(maxV)