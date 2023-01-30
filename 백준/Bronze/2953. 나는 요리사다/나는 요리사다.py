li = [list(map(int, input().split())) for _ in range(5)]
ans = 0
idx = 0
for i, l in enumerate(li):
    if sum(l) > ans:
        idx = i+1
        ans = sum(l)
print(idx, ans)