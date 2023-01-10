import sys

n, m = map(int, sys.stdin.readline().split())
not_hear = set()
not_seen = set()

for _ in range(n):
    not_hear.add(sys.stdin.readline().strip())

for _ in range(m):
    not_seen.add(sys.stdin.readline().strip())

ans = sorted(not_hear & not_seen)
print(len(ans))
for i in ans:
    print(i)
