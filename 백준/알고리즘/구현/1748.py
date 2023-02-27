def solution(n):
  l, ret = len(str(n)), 0
  for i in range(1, l):
    ret += i*(10**i-10**(i-1))
  ret += l*(n-10**(l-1)+1)
  return print(ret)

solution(int(input()))

"""
n,r = input(), 0
for i in range(len(n)):
  r += (int(n)-(10**i)+1)
print(r)
"""