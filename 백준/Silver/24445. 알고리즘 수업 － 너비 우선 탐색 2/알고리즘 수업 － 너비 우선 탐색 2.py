import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque()
cnt = 1
answer = [0 for _ in range(N+1)]
def bfs(n):
    global cnt
    visited[n] = True
    answer[n] = cnt
    cnt += 1
    que.append(sorted(graph[n], reverse=True))
    while que:
        temp = que.popleft()
        for t in temp:
            if not visited[t]:
                visited[t] = True
                que.append(sorted(graph[t], reverse=True))
                answer[t] = cnt
                cnt += 1
bfs(R)
print(*answer[1:], sep='\n')