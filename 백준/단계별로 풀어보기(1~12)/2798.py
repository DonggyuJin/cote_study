import sys
input = sys.stdin.readline

n,m=map(int,input().split())
card=sorted(list(map(int,input().split())), reverse=True)
x=0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            num = card[i]+card[j]+card[k]
            if num <= m: 
                if x < num: x = num
                break

print(x)


# n,m=map(int,input().split())
# card=sorted(list(map(int,input().split())))
# data=[]

# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             num = card[i]+card[j]+card[k]
#             if num <= m: data.append(num)

# if max(data) == m: print(m)
# else: print(max(data))
