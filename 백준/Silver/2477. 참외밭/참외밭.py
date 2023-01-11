k = int(input())

li = []
h = []
v = []
b_square = 0
s_square = 0

for i in range(6):
    d, l = map(int, input().split())
    li.append([d, l])
    if d == 1 or d == 2:
        h.append(l)
    else:
        v.append(l)

b_square = max(h) * max(v)

tmp = []
for i, l in enumerate(li):
    if l[0] == li[(i+2)%6][0]:
        tmp.append(li[(i+1)%6][1])
s_square = tmp[0] * tmp[1]

print(k * (b_square - s_square))