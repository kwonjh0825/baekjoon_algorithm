n = int(input())
li = list(map(int, input().split()))
v = int(input())
cnt = 0
for l in li:
    if l == v:
        cnt += 1
print(cnt)