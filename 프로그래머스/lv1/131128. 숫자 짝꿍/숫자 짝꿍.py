def solution(X:str, Y:str):
    answer = ''
    for i in range(10):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))
    if len(answer) < 1: 
        return '-1'
    elif set(list(answer)) == set(['0']):
        return '0'
    else: 
        return (''.join(sorted(answer, reverse=True)))

