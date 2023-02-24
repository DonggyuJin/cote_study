import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  cntZ = [1, 0]
  cntO = [0, 1]

  if n > 1:
    for i in range(n-1):
      cntZ.append(cntO[-1])
      cntO.append(cntZ[-2]+cntZ[-1])
  
  print(cntZ[n], cntO[n])