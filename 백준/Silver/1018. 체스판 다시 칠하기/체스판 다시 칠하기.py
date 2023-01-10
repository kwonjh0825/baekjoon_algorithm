n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(input()))
cnt = []
for i in range(n-7):
    for j in range(m-7):
        cnt_w = 0
        cnt_b = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if chess[a][b] == 'B':
                        cnt_w += 1
                    else:
                        cnt_b += 1
                else:
                    if chess[a][b] == 'B':
                        cnt_b += 1
                    else:
                        cnt_w += 1

        cnt.append(min(cnt_w, cnt_b))
print(min(cnt))