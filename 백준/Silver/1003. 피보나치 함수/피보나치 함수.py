import sys

input = sys.stdin.readline

def fibo(n):
    if len(zeros) <= n:
        for i in range(len(zeros), n+1):
            zeros.append(zeros[i-1] + zeros[i-2])
            ones.append(ones[i-1] + ones[i-2])
zeros = [1, 0, 1]
ones = [0, 1, 1]

T = int(input())
for _ in range(T):
    n = int(input())
    fibo(n)
    print(zeros[n], ones[n])