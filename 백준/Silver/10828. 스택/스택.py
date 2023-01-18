import sys

input = sys.stdin.readline
T = int(input())
li = []
for _ in range(T):
    a = input().strip()
    if a[:4] == 'push':
        li.append(a[5:])
    elif a == 'pop':
        print(li.pop() if li else -1)
    elif a == 'size':
        print(len(li))
    elif a == 'empty':
        print(1 if len(li) < 1 else 0)
    elif a == 'top':
        print(li[-1] if li else -1)
