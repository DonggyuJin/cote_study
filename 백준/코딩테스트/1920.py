import sys
input = sys.stdin.readline

n = int(input())
num = list(input().split())
m = int(input())
data = list(input().split())
num.sort()

def bin_search(target, lists):
    start = 0
    end = len(lists)-1

    while start <= end:
        mid = (start+end) // 2
        if lists[mid] == target:
            return print(1)
        elif lists[mid] < target:
            start = mid+1
        else:
            end = mid-1
    
    return print(0)

for i in range(m):
    bin_search(data[i], num)