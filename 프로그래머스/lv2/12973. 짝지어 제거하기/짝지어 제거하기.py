def solution(string:str):
    stack = []
    for s in string:
        if len(stack) == 0:
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)

    if stack:
        return 0
    else:
        return 1        