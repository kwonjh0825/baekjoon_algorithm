import sys
input = sys.stdin.readline

k = int(input())
li = []
for _ in range(k):
    n = int(input())
    if n:
        li.append(n)
    else:
        li.pop()
print(sum(li))
