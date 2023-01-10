import sys

n, m = map(int, sys.stdin.readline().split())
s = set()
for _ in range(n):
    s.add(sys.stdin.readline())

cnt = 0
for _ in range(m):
    if sys.stdin.readline() in s:
        cnt += 1
print(cnt)