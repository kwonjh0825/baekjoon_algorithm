n = int(input())
for i in range(1, n+1):
    sum = i
    li = list(map(int, str(i)))
    for l in li:
        sum += l
    if sum == n:
        print(i)
        break
else:
    print(0)