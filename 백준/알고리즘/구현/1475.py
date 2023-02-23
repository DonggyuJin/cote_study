import sys
input = sys.stdin.readline

n = input().rstrip()
k = {}

for num in range(0, 9): k[str(num)] = 0

for i in range(len(n)):
  if n[i] in ['6', '9']: k['6'] += 1
  else: k[n[i]] += 1

if k['6'] % 2 == 0: k['6'] //= 2
else: k['6'] = k['6']//2 + 1

print(max(k.values()))