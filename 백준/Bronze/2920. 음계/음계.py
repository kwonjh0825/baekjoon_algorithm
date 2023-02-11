li = list(map(int, input().split()))
if li == list(range(1, 9)):
    print('ascending')
elif li == list(range(8, 0, -1)):
    print('descending')
else:   
    print('mixed')