li = list(map(int, input().split()))
while li != sorted(li):
    for i in range(4):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            print(*li)