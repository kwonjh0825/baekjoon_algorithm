N = int(input())
li = list(map(int, input().split()))
up_cnt = 0
up_start = 0
ans = [0]

for i in range(1, len(li)):
    if li[i-1] < li[i] and up_cnt == 1:
        pass
    elif li[i-1] < li[i] and up_cnt == 0:
        up_start = li[i-1]
        up_cnt = 1
    elif not li[i-1] < li[i] and up_cnt == 1:
        ans.append(li[i-1] - up_start)
        up_start = 0
        up_cnt = 0
    else:
        up_cnt = 0
        up_start = 0
if up_cnt:
    ans.append(li[-1] - up_start)
print(max(ans))