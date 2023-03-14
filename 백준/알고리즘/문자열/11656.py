s = input()
rs = sorted([s[i:] for i in range(len(s))])
print(*rs, sep='\n')