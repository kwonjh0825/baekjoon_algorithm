N = input()
if len(N) < 2:
    N = '0' + N
new_num = N[-1] + str(sum(list(map(int, N))))[-1]
cnt = 1
while new_num != N:
    new_num = new_num[-1] + str(sum(list(map(int, new_num))))[-1]
    cnt += 1
print(cnt)
