import sys

n = int(sys.stdin.readline())

work = dict()
for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        work[name] = 1
    else:
        work[name] = 0
work = sorted(work.items(), reverse=True)
for w in work:
    if w[1] == 1:
        print(w[0])