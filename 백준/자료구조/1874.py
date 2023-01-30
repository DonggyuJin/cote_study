import sys
input = sys.stdin.readline

n = int(input())
data = []
result = []
i,j=0,1

for _ in range(n):
    num = int(input().rstrip())
    while j <= num:
        data.append(j)
        result.append('+')
        j+=1
    
    if data[-1] == num:
        data.pop()
        result.append('-')
    else:
        print("NO")
        i=1
        break

if i == 0: 
    for i in result : print(i)


"""
for _ in range(n): data.append(int(input().rstrip()))

num, result = [], []
i,j=0,1

while j<=n:
    if data[i] >= j:
        num.append(j)
        result.append('+')
        j+=1
    else:
        result.append('-')
        num.pop()
        i+=1

if data[-1:-(len(num)+1):-1] != num: print("NO")
else: print('\n'.join(result),'\n','\n'.join('-'*len(num)),sep='')
"""