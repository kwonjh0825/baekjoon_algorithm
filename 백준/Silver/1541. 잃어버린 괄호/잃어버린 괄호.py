string = input()

li = string.split('-')
ans = sum(list(map(int, li[0].split('+'))))
for l in li[1:]:
    ans -= sum(list(map(int, l.split('+'))))
print(ans)