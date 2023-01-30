import sys

input = sys.stdin.readline

M = int(input())

s = set()

for _ in range(M):
    command = input()

    if 'add' in command:
        s.add(int(command[4:]))

    elif 'remove' in command:
        if int(command[7:]) in s:
            s.remove(int(command[7:]))
        
    elif 'check' in command:
        if int(command[6:]) in s:
            print(1)  
        else:
            print(0)

    elif 'toggle' in command:
        if int(command[7:]) in s:
            s.remove(int(command[7:]))
        else:
            s.add(int(command[7:]))
    elif 'all' in command:
        s = set(range(1, 21))
    else:
        s = set()