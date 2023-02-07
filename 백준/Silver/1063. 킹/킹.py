a, b, n = input().split()
n = int(n)

direction = {'R': (1, 0), 'L': (-1, 0), 'B': (0, 1), 'T': (0, -1), 'RT': (1, -1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (-1, 1)}
king_x, king_y = ord(a[0]) - 65, 8 - int(a[1])
stone_x, stone_y = ord(b[0]) - 65, 8 - int(b[1])

for _ in range(n):
    t = input()
    nx, ny = king_x + direction[t][0], king_y + direction[t][1]
    if 0 <= nx < 8 and 0 <= ny < 8:
        if (nx, ny) == (stone_x, stone_y):
            stone_nx, stone_ny = stone_x + direction[t][0], stone_y + direction[t][1]
            if 0 <= stone_nx < 8 and 0 <= stone_ny < 8:
                stone_x, stone_y = stone_nx, stone_ny
                king_x, king_y = nx, ny
        else:
            king_x, king_y = nx, ny
print(f'{chr(king_x+65)}{8 - king_y}', f'{chr(stone_x+65)}{8-stone_y}', sep='\n')
