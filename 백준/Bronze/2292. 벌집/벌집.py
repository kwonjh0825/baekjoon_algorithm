import sys

n = int(sys.stdin.readline())
cnt = 1
num = 1
while n > num:
    num += cnt * 6
    cnt += 1
print(cnt)

