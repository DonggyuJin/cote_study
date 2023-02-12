import sys
input = sys.stdin.readline

def is_palindrome(word):
  return word == word[::-1]

while True:
  text = input().rstrip()
  if text == '0': break

  result = is_palindrome(text)
  if result: print('yes')
  else: print('no')