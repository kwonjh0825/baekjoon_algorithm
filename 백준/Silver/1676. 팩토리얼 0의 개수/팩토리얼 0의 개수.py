import sys, math

n = int(sys.stdin.readline())

fact_n = str(math.factorial(n))
cnt = 0
for s in fact_n[::-1]:
    if s == '0':
        cnt += 1
    else:
        print(cnt)
        break