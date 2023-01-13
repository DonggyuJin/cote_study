data=list(input())
nums=['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
count=0
for i in range(len(data)):
    for j in range(2, len(nums)):
        if data[i] in nums[j]:
            count+=j
            break
print(count+len(data))