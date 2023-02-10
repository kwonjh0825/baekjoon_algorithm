import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N = int(input())
li = [list(input().strip()) for _ in range(N)]
visited_rg = [[False] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
li_rg = []
cnt_rg = 0
cnt = 0
for l in li:
    li_rg.append(list(''.join(l).replace('R', 'G')))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if li[nx][ny] == li[x][y] and not visited[nx][ny]:
                dfs(nx, ny)

def dfs_rg(x, y):
    visited_rg[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if li_rg[nx][ny] == li_rg[x][y] and not visited_rg[nx][ny]:
                dfs_rg(nx, ny)

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1
        if not visited_rg[i][j]:
            dfs_rg(i, j)
            cnt_rg += 1
    
print(f'{cnt} {cnt_rg}')