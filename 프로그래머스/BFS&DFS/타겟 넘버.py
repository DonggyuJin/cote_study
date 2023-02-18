def solution(numbers, target):
    answer = 0
    
    q = [[0, 0]]
    
    while q:
        idx, num = q.pop()
        
        if idx < len(numbers):
            q.append([idx+1, num+numbers[idx]])
            q.append([idx+1, num-numbers[idx]])
        
        if idx == len(numbers):
            if num == target: answer += 1
    
    return answer