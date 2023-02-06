n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(s):
    stack = [s]
    visited[s] = True
    while stack:
        current = stack.pop()

        for adj in graph[current]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
dfs(1)

print(len([x for x in visited if x]) - 1)