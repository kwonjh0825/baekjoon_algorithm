import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin_li = sorted([int(input()) for _ in range(N)], reverse=True)
ans = 0
for coin in coin_li:
    if K // coin > 0:
        ans += K // coin
        K = K - (K//coin * coin)
    if not K:
        print(ans)
        break