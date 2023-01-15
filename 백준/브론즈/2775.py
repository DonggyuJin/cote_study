# T=int(input())
# for _ in range(T):
#     sums=0
#     k=int(input())
#     n=int(input())
#     if k==1:
#         for i in range(n,0,-1):
#             sums+=i
#         print(sums)
#     elif k>=2:
#         for i in range(k,0,-1):
#             for j in range(n,0,-1):
#                 sums+=j
#         print(sums)