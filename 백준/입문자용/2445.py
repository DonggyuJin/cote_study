n=int(input())
for i in range(1, n): print('*'*i, ' '*(2*(n-i)), '*'*i, sep='')
print('*'*(2*n))
for i in range(n-1, 0, -1): print('*'*i, ' '*(2*(n-i)), '*'*i, sep='')