input()
li = list(map(int, input().split()))
now = []
cnt = 0
for l in li:
    if l not in now:
        now.append(l)
    else:
        cnt += 1
print(cnt)