import sys
input = sys.stdin.readline

while True:
  n = int(input().rstrip())
  if n == -1: break
  
  rs = []
  for i in range(1, n+1):
    if n % i == 0: rs.append(i)
  
  result = rs[:len(rs)-1]
  if sum(result) == n: print(n, '=', ' + '.join(map(str, result)))
  else: print(n, 'is NOT perfect.')