import sys

input = sys.stdin.readline

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

n = int(input())
cnt = 0
for _ in range(n):
    cnt = cnt * 2 + 1
print(cnt)
hanoi(n, 1, 2, 3)