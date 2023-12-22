def solution(nums):
    answer = 0
    
    res = len(nums) / 2
    pok = set(nums)
    
    if len(pok) > res: answer = res
    else: answer = len(pok)
    
    return answer