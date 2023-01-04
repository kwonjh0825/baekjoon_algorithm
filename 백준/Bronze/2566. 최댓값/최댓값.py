arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))

max_value = 0
idx_r = 0
idx_c = 0

for i in range(9):
    if max(arr[i]) > max_value:
        max_value = max(arr[i])
        idx_r = i
        idx_c = arr[i].index(max_value)
print(max_value)
print(idx_r + 1, idx_c + 1)