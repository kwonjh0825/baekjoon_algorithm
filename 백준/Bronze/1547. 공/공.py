M = int(input())
ball = {1: 1, 2: 0, 3: 0}

for _ in range(M):
    x, y = map(int, input().split())
    if ball[x] or ball[y]:
        ball[x], ball[y] = ball[y], ball[x]

print(sorted(ball.items(), key=lambda x: -x[1])[0][0])