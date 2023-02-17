def solution(string):
    answer = []
    for s in list(string.lower().split(' ')):
        answer.append(s.capitalize())
    return ' '.join(answer)