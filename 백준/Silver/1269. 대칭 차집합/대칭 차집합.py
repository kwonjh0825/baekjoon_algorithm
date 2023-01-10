import sys

_, _ = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

a_b = a - b
b_a = b - a
print(len(a_b)+len(b_a))