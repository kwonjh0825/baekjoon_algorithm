li = [i for i in range(1, 31)]
for i in range(28):
    li.remove(int(input()))
li.sort()
for i in li:
    print(i)