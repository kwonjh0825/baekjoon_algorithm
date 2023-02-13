def solution(t, p):
    ans = 0
    len_p = len(p)
    for i in range(len(t)-len_p+1):
        if int(t[i:i+len_p]) <= int(p):
            ans += 1
    return ans
