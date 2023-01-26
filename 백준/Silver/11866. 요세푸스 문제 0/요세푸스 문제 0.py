from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
li = deque(range(1, n+1))
ans = []
while li:
    for _ in range(k-1):
        li.append(li.popleft())
    ans.append(li.popleft())
print('<', end='')
print(', '.join(map(str, ans)), end='')
print('>')