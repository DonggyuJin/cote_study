def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        # if i == j: 
        #     answer.append([array[i-1]][-1])
        #     continue
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer