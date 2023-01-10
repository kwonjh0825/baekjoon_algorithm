T = int(input())
for t in range(1, T+1):
    li = list(map(int, input().split()))
    print(f'#{t} {max(li)}')