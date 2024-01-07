def solution(price, money, count):
    answer = -1
    
    num = 0
    for i in range(1, count+1):
        num += price * i
        
    if money > num: return 0
    answer = abs(money - num)

    return answer