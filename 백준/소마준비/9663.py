import sys
input = sys.stdin.readline

n = int(input())
result = 0

def dfs(x, dr):
    global result
    if len(dr) == n:
        result += 1
        return
    
    for y in range(n):
        chk = True
        for row, col in dr:
            if y == col:
                chk = False
                break
            if abs(x-row) == abs(y-col):
                chk = False
                break

        if chk:
            dr.append((x, y))
            dfs(x+1, dr)
            dr.pop()

dfs(0, [])
print(result)