N = int(input())
li = [int(input()) for _ in range(N)]
print(*sorted(li), sep='\n')