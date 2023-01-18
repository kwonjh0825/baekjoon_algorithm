import sys

T = int(sys.stdin.readline())
for _ in range(T):
    li = list(sys.stdin.readline().split())
    for l in li:
        print(l[::-1], end=' ')
    print()