li = list(map(int, input().split()))
ans = 0
for l in li:
    ans += l**2
    
print(ans%10)