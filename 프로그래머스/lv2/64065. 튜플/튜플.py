def solution(string:str):
    string = string[1:-2]
    li = sorted(string.split('},'), key=lambda x:len(x))
    ans = []
    for s in li:
        s = list(map(int, s[1:].split(',')))
        for num in s:
            if num not in ans:
                ans.append(num)
    return ans