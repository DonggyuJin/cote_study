def solution(nums):
    answer = 0
    
    length = len(nums)//2
    if len(set(nums)) <= length: answer = len(set(nums))
    else: answer = length
    
    return answer