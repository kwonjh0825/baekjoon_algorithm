import sys

n = int(sys.stdin.readline())

work = dict()
for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        work[name] = 1
    else:
        work[name] = 0
print(*(sorted([w for w, s in work.items() if s == 1], reverse=True)), sep='\n')