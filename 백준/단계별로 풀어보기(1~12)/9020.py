from sys import stdin as ss

def is_prime(n):
    if n==1:
        return False
    for j in range(2,int(n**.5)+1):
        if n%j==0:
            return False
    return True

for _ in range(int(ss.readline())):
    n = int(ss.readline())
    a,b=n//2,n//2
    while a>0:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        else:
            a-=1
            b+=1


"""
def prime_number(mn):
    s = [True]*((2*mn)+1)
    s[0] = s[1] = False

    for i in range(2, int((2*mn)**0.5)+1):
        if s[i]:
            s[2*i::i] = (((2*mn)-i)//i) * [False]
    
    new=[]

    for i in range(len(s)):
        if s[i]:
            new.append(i)
    
    print(new)

    x=[]

    for i in range(len(new)):
        for j in range(i+1,len(new)):
            if new[j]+new[j]==mn:
                x.append(new[j])
            elif new[i]+new[j]==mn:
                x.extend([new[i], new[j]])
    
    x.sort()
    print(x)

    max_num = max(x[:len(x)//2])
    min_num = min(x[len(x)//2:])
    print(max_num, min_num)

n=int(sys.stdin.readline())
for _ in range(n):
    m=int(sys.stdin.readline())
    prime_number(m)
"""