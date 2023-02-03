import sys
input = sys.stdin.readline

while True:
    text = input().rstrip()
    if text == '.': break

    text = text.replace(" ", "")
    new_text = ''

    for i in range(len(text)):
        if text[i] == '[' or text[i] == ']' or text[i] == '(' or text[i] == ')' or text[i] == '.':
            new_text += text[i]
    
    while True:
        new_text = new_text.replace('()', "").replace('[]', "")
        if '()' in new_text or '[]' in new_text: 
            continue
        elif new_text == '.': 
            print('yes')
            break
        else: 
            print('no')
            break