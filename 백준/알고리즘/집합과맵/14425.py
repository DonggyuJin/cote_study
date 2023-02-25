import sys
input = sys.stdin.readline

n,m = map(int, input().split())
S = {input().rstrip() for _ in range(n)}
cnt = 0

for _ in range(m):
  text = input().rstrip()
  if S.__contains__(text): cnt += 1
print(cnt)

"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
S = {input().rstrip() for _ in range(n)}
cnt = 0

for _ in range(m):
  text = input().rstrip()
  if text in S: cnt += 1
print(cnt)
"""