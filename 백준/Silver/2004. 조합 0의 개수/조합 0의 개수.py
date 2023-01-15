import sys, math

def div_two(n):
    cnt = 0
    while n > 1:
        cnt += n // 2
        n = n // 2
    return cnt

def div_five(n):
    cnt = 0
    while n > 4:
        cnt += n // 5
        n = n // 5
    return cnt

n, m = map(int, sys.stdin.readline().split())
print(min(div_two(n)-div_two(n-m)-div_two(m), div_five(n)-div_five(n-m)-div_five(m)))
