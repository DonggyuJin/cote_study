import sys
input = sys.stdin.readline

n = int(input())
rs = [str(input().rstrip()) for _ in range(n)]
cnt = 0

while True:
  if len(rs[0]) == cnt:
    print(cnt)
    break
  
  new_rs = set()
  for i in rs:
    new_rs.add(i[len(i)-cnt:])

  if len(rs) == len(new_rs):
    print(cnt)
    break
  else:
    cnt += 1