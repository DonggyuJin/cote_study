import sys
ss = sys.stdin.readline

def merge_sort(A):
    if len(A) == 1:
        return A
    
    mid = (len(A) + 1)//2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    
    A2 = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A2.append(left[i])
            data.append(left[i])
            i += 1
        else:
            A2.append(right[j])
            data.append(right[j])
            j += 1
    
    while i < len(left):
        A2.append(left[i])
        data.append(left[i])
        i += 1
        
    while j < len(right):
        A2.append(right[j])
        data.append(right[j])
        j += 1
        
    return A2

n,k = map(int, ss().split())
a = list(map(int, ss().split()))

data = []
merge_sort(a)

if len(data) >= k:
    print(data[k-1])
else:
    print(-1) 