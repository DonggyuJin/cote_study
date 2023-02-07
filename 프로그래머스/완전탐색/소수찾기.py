from itertools import permutations

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    data = list(map(str, numbers))
    result = []
    for i in range(1, len(data)+1):
        result.append(list(set(permutations(data, i))))
    
    new = []
    for i in range(len(result)):
        for j in range(len(result[i])):
            new.append(int(''.join(result[i][j])))
            
    new = list(set(new))
    answer = 0
    for i in range(len(new)):
        if is_prime(new[i]) == True: answer+=1
        
    return answer