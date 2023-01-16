N = int(input())
score = list(map(int, input().split()))
ans, cnt = 0, 0
for s in score:
    if s:
        cnt += 1
        ans += cnt
    else:
        cnt = 0
print(ans)