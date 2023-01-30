import sys

input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0 
pr = []
for i in range(n):
    num = int(input())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        pr.append('+')

    if stack[-1] == num:
        stack.pop()
        pr.append('-')

    else:
        print('NO')
        break
else:
    print(*pr, sep='\n')