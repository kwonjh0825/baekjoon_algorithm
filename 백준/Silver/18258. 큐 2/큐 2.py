import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

N = int(input())

for _ in range(N):
    a = input().strip()
    
    if a.startswith('push'):
        queue.append(int(a[5:]))
    elif a == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif a == 'size':
        print(len(queue))
    elif a == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif a == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif a == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
