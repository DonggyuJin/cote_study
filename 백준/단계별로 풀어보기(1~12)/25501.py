def recursion(s, l, r, n):
    if l >= r: return 1,n+1
    elif s[l] != s[r]: return 0,n+1
    else: return recursion(s, l+1, r-1, n+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))
# print('ABCA:', isPalindrome('ABCA'))

n=int(input())
for _ in range(n):
    x=isPalindrome(input())
    print(x[0], x[1])

"""
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    cnt, p = 0, 1
    for i in range(len(s)//2):
        cnt += 1
        if s[i] != s[-(i+1)]:
            p = 0
            break
    if p: cnt += 1
    print(p, cnt)
"""