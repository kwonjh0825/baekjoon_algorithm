rect = []
x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    rect.append([a, b])

for i in x:
    for j in y:
        if [i, j] not in rect:
            print(i, j)
            break