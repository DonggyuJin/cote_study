def move(start, to):
    print(start, to)

def hanoi(n, start, to, via):
    if n==1: move(start, to)
    else:
        hanoi(n-1, start, via, to)
        move(start, to)
        hanoi(n-1, via, to, start)

n=int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)