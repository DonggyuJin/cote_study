import sys
input=sys.stdin.readline

N,M=map(int, input().split())
chess=[list(input().rstrip()) for _ in range(N)]
result=[]

for i in range(N-7):
    for j in range(M-7):
        notBlack = 0
        notWhite = 0
 
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if chess[a][b] != 'B':
                        notBlack += 1
                    elif chess[a][b] != 'W':
                        notWhite += 1
                else:
                    if chess[a][b] != 'W':
                        notBlack += 1
                    elif chess[a][b] != 'B':
                        notWhite += 1

        result.append(notBlack)
        result.append(notWhite)

print(min(result))