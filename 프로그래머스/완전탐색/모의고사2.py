def solution(answers):
    answer = []
    
    math1 = [1,2,3,4,5]
    math2 = [2,1,2,3,2,4,2,5]
    math3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == math1[i%5]: score[0] += 1
        if answers[i] == math2[i%8]: score[1] += 1
        if answers[i] == math3[i%10]: score[2] += 1
        
    for i in range(3):
        if max(score) == score[i]:
            answer.append(i+1)
    
    return answer