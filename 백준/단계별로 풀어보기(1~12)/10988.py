import sys
input = sys.stdin.readline

def is_palindrome(word):
  return word == word[::-1]

words = str(input().rstrip())
if is_palindrome(words): print(1)
else: print(0)