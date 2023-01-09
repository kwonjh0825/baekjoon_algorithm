import sys

T = int(sys.stdin.readline())

result = [False, False] + [True] * (10001)
for i in range(2, int(10001**1/2 + 1)):
    if result[i] == True:
        for j in range(i*2, 10001, i):
            result[j] = False

for _ in range(T):
    n = int(sys.stdin.readline())
    a, b = n // 2, n // 2
    while True:
        if result[a] and result[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1