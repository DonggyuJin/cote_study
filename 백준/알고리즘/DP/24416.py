import sys
input = sys.stdin.readline

n = int(input())
f = [0, 1, 1]
for i in range(3, n+1): 
    f.append(f[i-1]+f[i-2])
print(f[n], n-2)

"""
cnt1, cnt2 = 0, 0

def fib(n):
  global cnt1
  if n == 1 or n == 2:
    return cnt1  # 코드1
  else: 
    cnt1 += 1
    return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
  global cnt2
  f = [0,1,1]
  for i in range(3, n+1):
    cnt2 += 1
    f.append(f[i-1]+f[i-2])  # 코드2
  return f[n];

n = int(input())
fib(n)
fibonacci(n)
print(cnt1+1, cnt2)
"""