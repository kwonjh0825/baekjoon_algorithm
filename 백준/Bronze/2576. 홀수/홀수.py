num_li = [int(input()) for _ in range(7)]
odd_num = []
for num in num_li:
    if num % 2:
        odd_num.append(num)
if odd_num:
    print(sum(odd_num))
    print(min(odd_num))
else:
    print(-1)