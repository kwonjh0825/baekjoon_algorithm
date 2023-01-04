white = [[0 for i in range(100)] for i in range(100)]
n = int(input())
for i in range(n):
    r, c = map(int, input().split())
    for j in range(10):
        for k in range(10):
            white[r+j][c+k] = 1
cnt = 0

for w in white:
    for z in w:
        if z == 1:
            cnt += 1
print(cnt)