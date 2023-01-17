import sys
cnt_fib2 = 0

def fib2(n):
    global cnt_fib2
    fib = [1, 1]
    if n < 3:
        print(fib[n-1])
    else:
        for i in range(2, n):
            fib.append(fib[i-1]+fib[i-2])
            cnt_fib2 += 1
    return fib
N = int(sys.stdin.readline())
fib = fib2(N)
print(fib[N-1], cnt_fib2)