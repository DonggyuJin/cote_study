import sys
h,m=map(int,sys.stdin.readline().rstrip().split())
if h==0:
    if m < 45:
        print(23, ((h*60+m)-45)%60)
    else:
        print(0, ((h*60+m)-45)%60)
else:
    print(((h*60+m)-45)//60,((h*60+m)-45)%60)