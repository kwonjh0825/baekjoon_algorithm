from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
queue = deque()

for _ in range(T):
    a = input().split()
    if a[0] == 'push':
        queue.append(a[1])
    elif a[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if len(queue) < 1:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)