from collections import Counter

li = [int(input()) for _ in range(10)]
cnt = Counter(li)
sorted_cnt = sorted(cnt.items(), key=lambda x: -x[1])

print(sum(li)//10, sorted_cnt[0][0])