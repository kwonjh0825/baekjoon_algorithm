import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    box = []
    ans = 0
    m, n = map(int, input().split())
    for _ in range(m):
        box.append(list(map(int, input().split())))
    
    for i in range(n):
        cnt = 0
        for j in range(m-1, -1, -1):
            if box[j][i]:
                ans += cnt
            else:
                cnt += 1
    
    print(ans)