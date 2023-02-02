string = input().strip()
ans = []
for i in range(1, len(string)-1):
    for j in range(i+1, len(string)):
        a = string[:i]
        b = string[i:j]
        c = string[j:]
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        ans.append(a+b+c)
print(sorted(ans)[0])