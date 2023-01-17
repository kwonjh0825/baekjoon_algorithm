li = [int(input()) for _ in range(9)]
max = 0
idx = 0
for i, l in enumerate(li):
    if max < l:
        max = l
        idx = i + 1
print(max, idx, sep='\n')