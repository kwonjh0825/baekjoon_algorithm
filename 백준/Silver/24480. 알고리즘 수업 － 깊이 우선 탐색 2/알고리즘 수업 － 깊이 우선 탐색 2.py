import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i, g in enumerate(graph):
    graph[i] = sorted(g, reverse=True)

def dfs(node):
    global c
    c += 1
    visited[node] = True
    cnt[node] = c
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
c = 0
dfs(R)
print(*cnt[1:], sep='\n')
