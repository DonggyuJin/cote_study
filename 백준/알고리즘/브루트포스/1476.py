import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())
result = 1

tempE, tempS, tempM = 1, 1, 1
while True:
  
  if(tempE == E and tempS == S and tempM == M):
    break
  
  result += 1
  tempE += 1
  tempS += 1
  tempM += 1

  if(tempE > 15): tempE = 1
  if(tempS > 28): tempS = 1
  if(tempM > 19): tempM = 1

print(result)