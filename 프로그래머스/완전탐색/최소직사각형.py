def solution(sizes):
    answer = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1] != False:
            temp = sizes[i][1]
            sizes[i][1] = sizes[i][0]
            sizes[i][0] = temp
        else: continue
    
    data_left = []
    data_right = []
    
    for i in range(len(sizes)):
        data_left.append(sizes[i][0])
    for i in range(len(sizes)):
        data_right.append(sizes[i][1])
    
    answer = max(data_left)*max(data_right)
    
    return answer