import sys

n = int(sys.stdin.readline())
if n == 1:  
    print('1/1')
else:
    line = 0
    cnt = 0
    while cnt < n:
        line += 1
        cnt += line
    

    cnt = n - int((((line-1) * line) / 2))

    if line%2 == 1:
        upp = line
        low = 1
        for i in range(cnt-1):
            upp -= 1
            low += 1
    else:
        upp = 1
        low = line
        for i in range(cnt-1):
            upp += 1
            low -= 1
    print(f'{upp}/{low}')