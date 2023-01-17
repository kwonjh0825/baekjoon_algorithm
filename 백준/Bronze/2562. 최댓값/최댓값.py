a = [int(input()) for _ in range(9)]
print(max(a))
ind = 1

for j in range(9):
    if max(a) == a[j]:
        ind += j
        break
print(ind)