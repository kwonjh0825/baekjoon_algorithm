import sys
import math

N = int(sys.stdin.readline())
li = sorted([int(sys.stdin.readline()) for _ in range(N)])

res = []
for i in range(1, N):
    res.append(li[i] - li[i-1])

gcd = res[0]
for i in range(1, len(res)):
    gcd = math.gcd(gcd, res[i])

ans = set()
for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        ans.add(i)
        ans.add(gcd//i)
ans.add(gcd)

print(*sorted(ans))