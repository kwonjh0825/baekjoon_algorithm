ground = [[0] * 101 for _ in range(101)]
ans = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            ground[x][y] = 1
for g in ground:
    ans += g.count(1)
print(ans)