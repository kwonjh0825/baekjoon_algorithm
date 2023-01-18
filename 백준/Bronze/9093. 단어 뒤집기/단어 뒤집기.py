T = int(input())
for _ in range(T):
    li = list(input().split())
    for l in li:
        print(l[::-1], end=' ')
    print()