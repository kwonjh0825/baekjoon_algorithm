import sys

input = sys.stdin.readline

def draw_star(n):
    if n == 3:
        return ['***', '* *', '***']
    
    star = draw_star(n//3)
    stars = []
    for i in star:
        stars.append(i*3)
    for i in star:
        stars.append(i + ' '*(n//3) + i)
    for i in star:
        stars.append(i*3)
    
    return stars

print('\n'.join(draw_star(int(input()))))