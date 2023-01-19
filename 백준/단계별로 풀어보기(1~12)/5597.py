import sys
data=[]
for _ in range(1, 29):
    data.append(int(sys.stdin.readline().rstrip()))
no_send=[]
for i in range(1, 31):
    if i not in data:
        no_send.append(i)
no_send.sort()
print(no_send[0])
print(no_send[1])

"""
# 참고
n_list = [i for i in range(1,31)]
for i in range(28):
    n_list.remove((int(input())))
print(min(n_list))
print(max(n_list))
"""