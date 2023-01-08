data = input()
length = len(data)

for i in range(0, length+1, 10):
    if length < 11:
        print(data)
        break
    else:
        print(data[i:i+10])