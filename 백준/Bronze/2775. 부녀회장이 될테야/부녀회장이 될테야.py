import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    apt = []
    apt.append([x for x in range(1, n+1)])
    for i in range(k):
        tmp = []
        for j in range(1, n+1):
            tmp.append(sum(apt[i][:j]))
        apt.append(tmp)

    print(sum(apt[k-1][:n]))