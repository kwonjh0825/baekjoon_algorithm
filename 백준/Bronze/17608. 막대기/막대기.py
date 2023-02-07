import sys
input = sys.stdin.readline

N = int(input())
li = [int(input()) for _ in range(N)]
max_height = 0
cnt = 0
for l in reversed(li):
    if l > max_height:
        cnt += 1
        max_height = l
print(cnt)