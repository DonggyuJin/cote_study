import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pok = {}
for i in range(1, n+1):
  mon = str(input().rstrip())
  pok[i] = mon

reverse_pok = {v:k for k,v in pok.items()}

for _ in range(m):
  rs = input().rstrip()
  if rs.isdigit():
    print(pok[int(rs)])
  else:
    print(reverse_pok[rs])