import sys

input = sys.stdin.readline

N = int(input())
li = sorted(list(map(int, input().split())))
ans = 0
for _ in range(N):
    ans += sum(li)
    li.pop()
print(ans)
