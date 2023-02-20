import sys
input = sys.stdin.readline

s = input().rstrip()
rs = set()

for i in range(1, len(s)+1):
  for j in range(len(s)+1-i): rs.add(s[j:j+i])
print(len(rs))