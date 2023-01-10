import sys

s = sys.stdin.readline().strip()

ans = set()
for i in range(len(s) + 1):
    for j in range(i + 1, len(s) + 1):
        ans.add(s[i:j])
print(len(ans))