def solution(a, b, n):
    answer = 0
    
    while n >= a:
        cnt = n // a * b
        rest = n % a
        answer += cnt
        n = cnt + rest
    
    return answer