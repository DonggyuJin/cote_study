import sys
input = sys.stdin.readline

def is_palindrome(word):
  return str(word) == str(word)[::-1]

def is_prime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

n = input().rstrip()
rs = 0
for i in range(int(n), 1000001):
  if i == 1: continue
  if is_palindrome(i):
    if is_prime(i):
      rs = i
      break
if rs == 0: rs = 1003001

print(rs)