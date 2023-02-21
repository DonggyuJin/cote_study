import sys
input = sys.stdin.readline

grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total = 0
result = 0

for _ in range(20):
  a, b, c = map(str, input().rstrip().split())
  if c != 'P':
    total += float(b)
    result += float(b)*score[grade.index(c)]

print('%.6f' % (result/total))