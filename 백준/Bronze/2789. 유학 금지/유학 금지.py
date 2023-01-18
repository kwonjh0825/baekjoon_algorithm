name = input()
string = 'CAMBRIDGE'
ans = ''
for n in name:
    if n not in string:
        ans += n
print(ans)