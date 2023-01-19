from sys import stdin as ss
x,y,w,h=map(int,ss.readline().split())
print(min(x,y,w-x,h-y))

# if w-x == h-y: print(x)
# elif (w-x > x or w-x > y) and (h-y > x or h-y > y): print(x if x<y else y)
# elif w-x > h-y: print(h-y)
# elif w-x < h-y: print(w-x)