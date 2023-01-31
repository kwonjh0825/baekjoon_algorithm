import sys
input = sys.stdin.readline

N = int(input())
room = [list(input().strip()) for _ in range(N)]
rotated_room = [['']*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        rotated_room[i][j] = room[j][N-i-1]
ver_cnt = 0
hor_cnt = 0

for r, rr in zip(room, rotated_room):
    len_r = 0
    len_rr = 0
    for i in range(N):
        if r[i] == '.':
            len_r += 1
        elif r[i] == 'X':
            if len_r > 1:
                hor_cnt += 1
                len_r = 0
            else:
                len_r = 0
        
        if rr[i] == '.':
            len_rr += 1
        elif rr[i] == 'X':
            if len_rr > 1:
                ver_cnt += 1
                len_rr = 0
            else:
                len_rr = 0
    
    if len_r > 1:
        hor_cnt += 1                
    if len_rr > 1:
        ver_cnt += 1

print(hor_cnt, ver_cnt)
