li = []
for i in range(5):
    li.append(list(input().strip()))
    if len(li[i]) < 15:
        li[i].extend([0] * (15 - len(li[i])))

for i in range(15):
    for j in range(5):
        if li[j][i] == 0:
            continue
        else:
            print(li[j][i], end='')
