import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(a):
    visited[a] = True
    for i in graph[a]:
        if not visited[i]:
            dfs(i)

for k in range(1, N+1):
    if not visited[k]:
        dfs(k)
        cnt += 1

print(cnt)
