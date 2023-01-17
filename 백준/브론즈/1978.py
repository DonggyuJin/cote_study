N=int(input())
data=list(map(int, input().split()))
count=0
for i in range(N):
    count+=1
    for j in range(2,data[i]):
        if data[i]%j==0:
            count-=1
            break
if 1 in data:
    count-=1
print(count)