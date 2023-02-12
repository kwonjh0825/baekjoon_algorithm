import sys
from collections import deque

input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
stack = []
while True:
    for s in string:
        stack.append(s)
        if stack[-len(bomb):] == list(bomb):
            for _ in range(len(bomb)):
                stack.pop()

    string = ''.join(stack)
    if bomb not in string:
        break

if string:
    print(string)
else:
    print('FRULA')