import sys

def prime_number(mn,mx):
    data = []
    s = [True]*(mx+1)
    s[0] = s[1] = False

    for i in range(2, mx+1):
        if s[i]:
            for j in range(2*i, mx+1, i):
                s[j] = False

    # 위와 똑같지만, 시간 복잡도에서 차이가 남
    # 아래 코드가 더 효율적
    # for i in range(2, int(mx**0.5)+1):
    #     if s[i]:
    #         s[2*i::i] =  ((mx-i)//i) * [False]
    # print('\n'.join(f'{i}' for i in range(mn, mx+1) if s[i]))
    
    for i in range(mn, mx+1):
        if s[i]:
            data.append(i)
    
    if data:
        for i in range(len(data)):
            print(data[i])

M,N=map(int, sys.stdin.readline().split())

prime_number(M,N)