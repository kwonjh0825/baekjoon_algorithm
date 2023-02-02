T = int(input())
for _ in range(T):
    li = sorted(list(map(int, input().split())))
    if li[-2] - li[1] > 3:
        print('KIN')
    else:
        print(sum(li[1:4]))