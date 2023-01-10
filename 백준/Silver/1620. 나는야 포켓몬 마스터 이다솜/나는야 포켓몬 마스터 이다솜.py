import sys

n, m = map(int, sys.stdin.readline().split())
dict_pocket = {}
for i in range(1, n+1):
    p_name = sys.stdin.readline().strip()
    p_name[1:].lower()
    dict_pocket[i] = p_name
    dict_pocket[p_name] = i

for i in range(m):
    n = sys.stdin.readline().strip()
    if n.isalpha():
        print(dict_pocket[n])             
    else:
        print(dict_pocket[int(n)])
