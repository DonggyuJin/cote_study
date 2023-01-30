import sys
input = sys.stdin.readline

text = list(input().rstrip())
n = int(input())

new_text = []
for _ in range(n):
    command = list(input().split())
    if command[0] == 'L':
        if text: new_text.append(text.pop())
    elif command[0] == 'D':
        if new_text: text.append(new_text.pop())
    elif command[0] == 'B':
        if text: text.pop()
    else: text.append(command[1])

text.extend(reversed(new_text))
print(''.join(text))

"""
command = []

for _ in range(n):
    cmd = input().rstrip()
    if 'P' in cmd:
        command.append(list(cmd.split(' ')))
    else: command.append(cmd)

L=len(text)
for i in range(len(command)):
    if L < 0:
        L = 0
    if command[i] == 'L':
        L -= 1
    elif command[i] == 'D':
        L += 1
    elif command[i] == 'B':
        if L-1 >= 0: 
            del text[L-1]
            L -= 1
    else: 
        text.insert(L, command[i][1])
        L+=1

print(*text, sep='')
"""