from collections import Counter
import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()

print(round((sum(li))/len(li)))

if len(li) % 2 == 0:
    print((li[len(li)/2] + li[(len(li)/2)-1]) / 2)
else:
    print(li[len(li)//2])

cnt = Counter(li).most_common(2)
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(li)-min(li))