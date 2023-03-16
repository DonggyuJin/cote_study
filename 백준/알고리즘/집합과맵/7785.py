import sys
input = sys.stdin.readline

n = int(input())
rs = {}
for _ in range(n):
  nick, stat = map(str, input().rstrip().split())
  if stat == "enter": rs[nick] = stat
  elif stat == "leave":
    if nick in rs: del(rs[nick])
print(*sorted(rs, reverse=True), sep='\n')