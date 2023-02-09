n = int(input())
ans = [0, 0, 1, 2]

if n < 4:
    print(n)
else:
    for i in range(4, n+2):
        ans.append(ans[i-1]+ans[i-2])
    print(ans[-1]%10007)