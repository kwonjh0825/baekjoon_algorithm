n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

li.sort()

for i in li:
    print(i[0], i[1])