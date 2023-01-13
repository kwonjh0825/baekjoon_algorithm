import sys
import math

N = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

a = li[0]

for l in li[1:]:
    print(f'{a//math.gcd(a, l)}/{l//math.gcd(a, l)}')