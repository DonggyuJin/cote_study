n=int(input())
count=n
for i in range(n):
    a=input()
    for j in range(0, len(a)-1):
        if a[j]==a[j+1]:
            pass
        elif a[j] in a[j+1:]:
            count-=1
            break
print(count)