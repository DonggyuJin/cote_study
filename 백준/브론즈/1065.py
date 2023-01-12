def hanFunc(n):
    count=0
    for i in range(1,n+1):
        data=list(map(int,str(i)))
        if i<100:
            count+=1
        elif data[0]-data[1]==data[1]-data[2]:
            count+=1
    return print(count)
hanFunc(int(input()))

"""
N=int(input())
count=0
for i in range(1,N+1):
    data=list(map(int,str(i)))
    if i<100:
        count+=1
    elif data[0]-data[1]==data[1]-data[2]:
        count+=1
print(count)
"""

"""
data=[111,123,135,147,159,210,222,234,246,257,321,333,345,357,369,420,432,444,456,468,531,543,555,567,579,630,642,654,666,678,741,753,765,777,781,840,852,864,876,888,951,963,975,987,999]
for i in range(1,N+1):
    if i<10:
        count+=1
    elif 10<=i<100:
        count+=1
    elif 100<=i<=1000:
        if i in data:
            count+=1
"""