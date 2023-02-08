import sys
from collections import deque
input = sys.stdin.readline

card = deque(list(map(str, range(1, int(input())+1))))

while len(card) > 1:
  card.popleft()
  x = card[0]
  card.popleft()
  card.append(x)

print(card[0])