# n=int(input())
# num=n
# a,b,x=0,1,0

# while n>1:
#     x=a+b
#     a=b
#     b=x
#     n-=1

# if num==1:print(1)
# elif num<=20:print(x)


def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))
