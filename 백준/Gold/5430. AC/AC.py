import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    command = input().strip()
    n = int(input())
    if n:
        li = input().strip()[1:-1]
        li = deque(list(map(int, li.split(','))))
    else:
        input()
        li = deque()
    flag_r = 0

    for c in command:
        if c == 'R':
            flag_r += 1
        elif li and flag_r % 2:
            li.pop()
        elif li and flag_r % 2 == 0:
            li.popleft()
        else:
            print('error')
            break
    else:
        if flag_r % 2:
            li.reverse()
        print('[', end='')
        print(*li, sep=',',end='')
        print(']')