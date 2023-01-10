n = int(input())
li = []
cnt_list = []
for i in range(n):
    li.append(list(map(int, input().split())))
for i in li:
    cnt = 0
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    cnt += 1
    cnt_list.append(cnt)

for i in cnt_list:
    print(i, end=' ')