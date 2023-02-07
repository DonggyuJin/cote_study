def solution(arr):
    answer = []
    
    for i in range(0, len(arr)-1):
        if arr[i] != arr[i+1]: answer.append(arr[i])
        else: continue
    
    if len(answer) > 0: 
        if arr[-1] != answer[-1]: answer.append(arr[-1])
    else: answer = list(set(arr))
    
    return answer