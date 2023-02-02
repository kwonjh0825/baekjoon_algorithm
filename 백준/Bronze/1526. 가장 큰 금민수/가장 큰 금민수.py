for i in range(int(input()), 1, -1):
    for s in str(i):
        if s in '01235689':
            break
    else:
        print(i)
        break