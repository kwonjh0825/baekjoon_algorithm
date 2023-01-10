import sys

n = int(sys.stdin.readline())
li = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

for c in compare:
    if c in li:
        print(1, end=' ')
    else:
        print(0, end=' ')
