def solution(brown, yellow):
    answer = []
    
    n = brown + yellow
    
    for i in range(3, int(n/2)+1):
        j = n / i
        
        if (j*10) % 10 != 0 : continue
        
        if (i-2) * (j-2) == yellow:
            answer.append(i)
            answer.append(int(j))
            break
            
    if answer[0] < answer[1]:
        answer.sort(reverse=True)
    
    return answer

    # result = brown + yellow
    # n = result // 2
    
    # data = []
    # for i in range(1, n+1):
    #     if result % i == 0: 
    #         data.append(i)
    #         data.append(result//i) 
    # data = sorted(list(set(data)))
    
    # l = len(data)
    # if l%2 == 0: answer = [data[l//2], data[l//2-1]]
    # else: answer = [data[l//2], data[l//2]]
    
    # return answer