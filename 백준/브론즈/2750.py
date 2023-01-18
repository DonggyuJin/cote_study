N=int(input())
data=[]

# for _ in range(N): data.append(int(input()))
# for j in range(N):
#     for i in range(N-1):
#         temp=0
#         if data[i] > data[i+1]:
#             temp=data[i+1]
#             data[i+1]=data[i]
#             data[i]=temp

# for i in range(len(data)):print(data[i])
# 정렬함수 이용
data.sort()
for i in data:print(i, sep='\n')