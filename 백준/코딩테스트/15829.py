import sys
input = sys.stdin.readline

l = int(input())
text = input().rstrip()
cnt = 0

for i in range(l):
  cnt += (ord(text[i])-96) * (31**i)
print(cnt % 1234567891)