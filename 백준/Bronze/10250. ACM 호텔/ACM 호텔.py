import sys, math

t = int(sys.stdin.readline())
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    num = 1
    while h < n:
        num += 1
        n -= h
    if len(str(num)) < 2:
        print(str(n)+'0'+str(num))
    else:
        print(str(n)+str(num))