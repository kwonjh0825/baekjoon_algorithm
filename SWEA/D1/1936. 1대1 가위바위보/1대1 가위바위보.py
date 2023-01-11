
a, b = map(int, input().split())
result = [0, 1, 2, 3, 1]

if result[b] == result[a+1]:
    print('B')
else:
    print('A')