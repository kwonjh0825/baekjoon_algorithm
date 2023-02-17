def solution(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True