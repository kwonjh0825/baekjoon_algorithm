a = list(int(input()) for i in range(10))
remain_set = []
for j in range(10):
    remain_set.append(a[j]%42)
ans = list(set(remain_set))
print(len(ans))