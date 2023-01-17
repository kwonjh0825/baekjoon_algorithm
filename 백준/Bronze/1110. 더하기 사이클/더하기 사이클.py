n = int(input())
if n < 10:
    list_n = [0, n]
else:
    list_n = [int (a) for a in str(n)]
origin_n = list_n
t = cycle = int()
while(1):
    t = [int(b) for b in str(sum(list_n))]
    if sum(list_n) < 10:
        list_n = [list_n[1], t[0]]
    else:
        list_n = [list_n[1], t[1]]
    cycle += 1
    if list_n == origin_n:
        break
print(cycle)