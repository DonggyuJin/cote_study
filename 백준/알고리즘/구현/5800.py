import sys
input = sys.stdin.readline

k = int(input())
for i in range(1, k+1):
  data = list(map(int, input().split()))
  n, score = data[0], sorted(data[1:], reverse=True)
  cnt = 0
  for j in range(n-1):
    cnt = max(cnt, score[j]-score[j+1])
  print(f'Class {i}')
  print(f'Max {max(score)}, Min {min(score)}, Largest gap {cnt}')