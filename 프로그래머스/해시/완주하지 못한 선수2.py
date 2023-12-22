def solution(participant, completion):
    answer = ''
    
    new = {}
    
    for val in participant:
        if val not in new:
            new[val] = 1
            continue
        new[val] += 1
    
    for user in completion:
        new[user] -= 1
        
    for k, v in new.items():
        if v == 1: answer = k
        
    return answer