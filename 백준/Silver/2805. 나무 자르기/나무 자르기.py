import sys
input = sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))
start, end = 0, max(li)

while start <= end:
    mid = (start + end) // 2

    cnt_wood = 0
    for l in li:
        if l > mid:
            cnt_wood += (l - mid)

    if cnt_wood >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)