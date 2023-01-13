import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    dict_wear = {}
    for i in range(n):        
        _, classify = sys.stdin.readline().split()
        dict_wear[classify] = dict_wear.get(classify, 0) + 1
    result = 1
    for d in dict_wear.values():
        result *= d + 1

    print(result-1)