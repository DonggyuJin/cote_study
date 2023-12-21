def solution(sizes):
    answer = 0
    
    rw, rh = 0, 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
        
    for size in sizes:
        w, h = size[0], size[1]
        
        rw, rh = max(rw, w), max(rh, h)
        
    answer = rw * rh
    
    return answer