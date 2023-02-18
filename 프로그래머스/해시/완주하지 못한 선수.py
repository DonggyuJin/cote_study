def solution(participant, completion):
    
    hashDict = {}
    sumHash = 0
    
    for i in participant:
        hashDict[hash(i)] = i
        sumHash += hash(i)
    
    for i in completion:
        sumHash -= hash(i)
    
    print(hashDict)
    print(sumHash)
    return hashDict[sumHash]