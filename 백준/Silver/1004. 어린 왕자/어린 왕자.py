import sys
import math


T = int(sys.stdin.readline())
for _ in range(T):
    d_x, d_y, a_x, a_y = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    cnt = 0
    for _ in range(n):
        c_x, c_y ,c_r = map(int, sys.stdin.readline().split())
        distance_d_to_c = math.sqrt((c_x-d_x)**2 + (c_y-d_y)**2)
        distance_a_to_c = math.sqrt((c_x-a_x)**2 + (c_y-a_y)**2)
        
        if (distance_d_to_c < c_r and distance_a_to_c > c_r) or (distance_a_to_c < c_r and distance_d_to_c > c_r):
            cnt += 1

    print(cnt)