import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

li = deque(list(range(1, N+1)))
target = list(map(int, input().split()))
cnt = 0

while target:
    t = target[0]
    if li[0] == t:
        li.popleft()
        target.remove(t)
    elif li.index(t) < (len(li) // 2) + 1:
        li.append(li.popleft())
        cnt += 1
    else:
        li.appendleft(li.pop())
        cnt += 1
print(cnt)
    
