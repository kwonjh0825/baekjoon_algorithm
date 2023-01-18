import sys
input = sys.stdin.readline

input()
a_list = set(map(int, input().split()))
input()
m_list = list(map(int, input().split()))

for m in m_list:
    if m in a_list:
        print(1)
    else:
        print(0)