import sys
input = sys.stdin.readline

def drawing_star(l):
    if l==1: return ['*']

    star = drawing_star(l//3)
    data = []

    for s in star:
        data.append(s*3)
    for s in star:
        data.append(s+' '*(l//3)+s)
    for s in star:
        data.append(s*3)
    return data

N=int(input().rstrip())
print('\n'.join(drawing_star(N)))