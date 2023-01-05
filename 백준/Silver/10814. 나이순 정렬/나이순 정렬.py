import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    li.append([int(age), name])

li.sort(key=lambda x:x[0])

for i in li:
    print(i[0], i[1])