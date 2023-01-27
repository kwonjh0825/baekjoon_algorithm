import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    que = deque(map(int, input().split()))
    cnt = 0
    idx = deque([0] * (n))
    idx[m] = 1
    while que:
        if que[0] == max(que):
            cnt += 1
            if idx[0]:
                print(cnt)
                break
            else:
                que.popleft()
                idx.popleft()
        else:
            idx.append(idx.popleft())
            que.append(que.popleft())
