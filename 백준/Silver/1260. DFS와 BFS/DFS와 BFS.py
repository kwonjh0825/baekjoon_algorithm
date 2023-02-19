import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M, R = map(int, input().split())
visited_bfs = [False] * (N+1)
visited_dfs = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque()

def dfs(n):
    visited_dfs[n] = True
    print(n, end=' ')
    for i in sorted(graph[n]):
        if not visited_dfs[i]:
            dfs(i)

def bfs(n):
    visited_bfs[n] = True
    print(n, end= ' ')
    que.append(sorted(graph[n]))
    while que:
        temp = que.popleft()
        for t in temp:
            if not visited_bfs[t]:
                visited_bfs[t] = True
                que.append(sorted(graph[t]))
                print(t, end=' ')

dfs(R)
print()
bfs(R)