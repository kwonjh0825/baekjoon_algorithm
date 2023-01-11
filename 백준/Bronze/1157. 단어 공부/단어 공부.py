a = input().upper()
a_list = list(set(a))
cnt = []

for i in a_list:
    cnt.append(a.count(i))

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(a_list[cnt.index(max(cnt))])