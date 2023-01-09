import sys

def is_prime(n):
    result = [False, False] + [True] * ((2*n) + 1)
    cnt = 0
    for i in range(2, int((2 * n)**1/2 + 1)):
        if result[i] == True:
            for j in range(i*2, (2*n) + 1, i):
                result[j] = False
    for i in range(n + 1, (2*n) + 1):
        if result[i] == True:
            cnt += 1
    print(cnt)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        is_prime(n)
