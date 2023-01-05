import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(sys.stdin.readline().strip())
li = list(set(li))
li.sort()
li.sort(key=lambda x: len(x))

for l in li:
    print(l)