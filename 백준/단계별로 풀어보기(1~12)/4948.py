import sys

def prime_number(mn):
    s = [True]*((2*mn)+1)
    s[0] = s[1] = False

    for i in range(2, int((2*mn)**0.5)+1):
        if s[i]:
            s[2*i::i] = (((2*mn)-i)//i) * [False]
    
    new=s[mn+1:(2*mn)+1]
    print(new.count(True))

while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    prime_number(n)