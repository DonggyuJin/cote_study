import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	a, b = map(int,input().split())
	a2 = a % 10

	if a2 == 0: print(10)
	elif a2 in [1,5,6]: print(a2)
	elif a2 in [4,9]:
		b2 = b % 2
		if b2 == 0: print(a2 * a2 % 10)
		else: print(a2)
	else:
		b2 = b % 4  
		if b2 == 0: print(a2 ** 4 % 10)
		else: print(a2 ** b2 % 10)