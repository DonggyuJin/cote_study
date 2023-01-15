t=int(input())
for _ in range(t):
    k=int(input())
    n=int(input())
    data=[i for i in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            data[j]+=data[j-1]
    print(data[-1])