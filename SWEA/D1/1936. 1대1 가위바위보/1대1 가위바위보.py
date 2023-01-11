a, b = map(int, input().split())
if a < 3:
    if b == (a + 1):
        print('B')
    else:
        print('A')
else:
    if b == 1:
        print('B')
    else:
        print('A')