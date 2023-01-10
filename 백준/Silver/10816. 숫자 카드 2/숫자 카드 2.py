import sys
from collections import Counter

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

result = Counter(li)

for i in compare:
    if i in result.keys():
        print(result[i], end=' ')
    else:
        print(0, end=' ')