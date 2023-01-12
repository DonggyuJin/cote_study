data=input().lower()
new=list(set(data))
cnt=[]
for i in new:
    count=data.count(i)
    cnt.append(count)
if cnt.count(max(cnt))>=2: print('?')
else: print(new[(cnt.index(max(cnt)))].upper())