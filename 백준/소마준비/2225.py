import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def fac(n):
  sum = 1
  for i in range(1, n+1):
    sum *= i
  return sum

print(fac(n+k-1)//(fac(k-1)*fac(n))%1000000000)