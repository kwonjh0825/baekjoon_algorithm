import sys
input = sys.stdin.readline

n = int(input())
ans = [0, 1, 3]

if n < 3:
    print(ans[n])
else:
    for i in range(3, n+1):
        ans.append(ans[i-1]+ (2*ans[i-2]))
    print(ans[-1]%10007)