T = int(input())
for _ in range(T):
    string = input()
    stack = []

    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')