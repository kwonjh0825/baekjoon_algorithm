import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

li = []
for _ in range(N):
    li += map(int, input().split())
ans = []

for i in range(min(li), max(li) + 1):
    block = B
    time = 0
    for l in li:
        if (l - i) > 0:
            block += (l-i)
            time += 2 * (l-i)
        else:
            block -= (i-l)
            time += (i-l)
    if block > -1:
        ans.append((time, i))
print(*sorted(ans,key=lambda x: (x[0], -x[1]))[0])