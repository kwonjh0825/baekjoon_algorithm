from collections import deque

n = int(input())
li = deque(x for x in range(1, n+1))
for _ in range(n):
    print(li.popleft())
    if li:
        li.append(li.popleft())
