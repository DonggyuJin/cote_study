def solution(n, computers):
    answer = 0
    chk = [0] * n
    
    def dfs(v):
        chk[v] = 1
        
        for i in range(n):
            if not chk[i] and computers[v][i]:
                dfs(i)
    
    for i in range(n):
        if not chk[i]:
            dfs(i)
            answer += 1
    
    return answer