import sys
ss = sys.stdin.readline

N=int(input())
data = [int(ss()) for _ in range(N)]
data.sort()

for i in data:print(i, sep='\n')

# data=[]
# for _ in range(N): data.append(int(input()))
# for j in range(N):
#     for i in range(N-1):
#         temp=0
#         if data[i] > data[i+1]:
#             temp=data[i+1]
#             data[i+1]=data[i]
#             data[i]=temp

# for i in range(len(data)):print(data[i])