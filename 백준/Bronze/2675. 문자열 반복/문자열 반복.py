N = int(input())

for _ in range(N):
    p, string = input().split()
    p = int(p)
    for s in string:
        print(s*p, end='')
    print()
