num_li = sorted(map(int, input().split()))

t = len(set(num_li))
if t == 1:
    print(10000+(num_li[0]*1000))
elif t == 2:
    print(1000+(num_li[1]*100))
else:
    print(100*(max(num_li)))
