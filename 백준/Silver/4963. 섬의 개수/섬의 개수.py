import sys
sys.setrecursionlimit(10000)

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    
    ans = 0
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    visited = [[False] * w for _ in range(h)]
    
    def dfs(x, y):
        visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] and not visited[nx][ny]:
                    dfs(nx, ny)
    
    for x in range(h):
        for y in range(w):
            if graph[x][y] and not visited[x][y]:
                dfs(x, y)
                ans += 1
    print(ans)