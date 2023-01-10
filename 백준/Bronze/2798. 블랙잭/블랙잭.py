from itertools import combinations

n, m = map(int, input().split())
li = list(map(int, input().split()))

combs = list(combinations(li, 3))
ans = 0
for c in combs:
    if sum(c) > m:
        continue
    elif sum(c) > ans:
        ans = sum(c)
print(ans)
