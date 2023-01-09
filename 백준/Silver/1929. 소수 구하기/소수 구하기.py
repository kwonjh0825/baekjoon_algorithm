import sys

def is_prime(m, n):
    result = [False, False] + ([True] * (n-1))
    sum = 0
    for i in range(2, int(n**1/2) + 1):
        if result[i] == True:
            for j in range(i*2, n+1, i):
                result[j] = False
    for i in range(m, n+1):
        if result[i] == True:
            print(i)
                
m, n = map(int, sys.stdin.readline().split())

is_prime(m, n)