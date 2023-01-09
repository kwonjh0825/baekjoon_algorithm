def is_prime(n):
    result = [False, False] + ([True] * (n-1))

    for i in range(2, int(n**1/2) + 1):
        if result[i] == True:
            for j in range(i*2, n+1, i):
                result[j] = False
            
    return True if result[n] == True else False

n = int(input())
li = list(map(int, input().split()))
cnt = 0

for i in li:
    if is_prime(i):
        cnt += 1
print(cnt)
