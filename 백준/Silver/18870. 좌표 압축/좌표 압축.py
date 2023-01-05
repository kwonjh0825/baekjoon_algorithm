import sys

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
ans = sorted(list(set(li)))

ans_dict = {ans[i]: i for i in range(len(ans))}

for i in li:
    print(ans_dict[i], end=' ')