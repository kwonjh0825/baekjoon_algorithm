import sys, heapq

input = sys.stdin.readline

h = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(h, (-x, x))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)