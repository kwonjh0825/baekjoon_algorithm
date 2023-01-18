string = input()
for i in range(0, 100, 10):
    s = string[i:i+10]
    if s:
        print(s)
    else:
        break
