import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx] and graph[ny][nx]:
                dfs(ny, nx)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]    
    cnt = 0

    for _ in range(K):
        j, i = map(int, input().split())    # (가로위치, 세로위치) 순으로 입력
        graph[i][j] = 1                     # 배열에서는 (세로위치, 가로위치) 순으로 접근
    
    for j in range(M):
        for i in range(N):
            if not visited[i][j] and graph[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)