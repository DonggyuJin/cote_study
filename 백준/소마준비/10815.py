import sys
input = sys.stdin.readline

n = int(input())
num = list(map(str, input().split()))
num.sort()

m = int(input())
data = list(map(str, input().split()))
# result = []

def bisect_search(target, lists):
  start = 0
  end = len(lists) - 1

  while start <= end:
    mid = (start+end) // 2
    if lists[mid] == target: 
      return mid
    elif lists[mid] < target: start = mid+1
    else: end = mid - 1

  return None

for i in range(len(data)):
  if bisect_search(data[i], num) is not None: print(1, end=' ')
  else:  print(0, end=' ')

# def bisect_search(target, lists):
#   start = 0
#   end = len(lists) - 1

#   while start <= end:
#     mid = (start+end) // 2
#     if lists[mid] == target: 
#       return result.append(1)
#     elif lists[mid] < target: start = mid+1
#     else: end = mid - 1

#   return result.append(0) 

# for i in range(len(data)): bisect_search(data[i], num)

# print(*result, sep=' ')