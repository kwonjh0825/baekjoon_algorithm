import sys

def is_prime(m, n):
    result = [False, False] + ([True] * (n-1))
    sum = 0
    for i in range(2, int(n**1/2) + 1):
        if result[i] == True:
            for j in range(i*2, n+1, i):
                result[j] = False
    try:
        idx = result.index(True, m, n+1)
        for i in range(m, n+1):
            if result[i] == True:
                sum += i
        return sum, idx
    except:
        return -1, -1
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

sum, idx = is_prime(m, n)
if sum == -1:
    print(-1)
else:
    print(sum)
    print(idx)
