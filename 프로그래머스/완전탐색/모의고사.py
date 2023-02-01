def solution(answers):
    answer = []
    
    one = [1,2,3,4,5] * 2000
    two = [2,1,2,3,2,4,2,5] * 1250
    three = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    a,b,c=0,0,0
    
    for i in range(len(answers)):
        if answers[i] == one[i]: a+=1
        if answers[i] == two[i]: b+=1
        if answers[i] == three[i]: c+=1
        
    m = max(a,b,c)
    
    if m == a and m == b and m == c: answer = [1, 2, 3]
    elif m == a and m == b and m != c: answer = [1, 2]
    elif m == a and m != b and m == c: answer = [1, 3]
    elif m != a and m == b and m == c: answer = [2, 3]
    elif m == a: answer = [1]
    elif m == b: answer = [2]
    elif m == c: answer = [3]

    return answer