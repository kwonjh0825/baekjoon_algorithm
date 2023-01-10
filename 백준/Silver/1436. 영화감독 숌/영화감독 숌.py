import sys

n = int(sys.stdin.readline())
li = []
i = 1
while len(li) < 10001:
    if '666' in str(i):
        li.append(i)
    i += 1
print(li[n-1])