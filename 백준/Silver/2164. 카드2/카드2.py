from collections import deque
import sys

n = int(sys.stdin.readline())
li = deque(i for i in range(1, n+1))

while len(li) > 1:
    li.popleft()
    li.append(li.popleft())
print(li[0])