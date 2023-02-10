import sys
input = sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))
for i in range(N-1):
    li[i+1] += li[i]

li = [0] + li

for _ in range(M):
    i, j = map(int, input().split())
    print(li[j] - li[i-1])