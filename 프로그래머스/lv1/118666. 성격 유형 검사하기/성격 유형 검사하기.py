def solution(survey, choices):
    answer = ''
    li = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    dict_survey = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for sur, choi in zip(survey, choices):
        sur_a, sur_b = sur[0], sur[1]
        if choi < 4:
            dict_survey[sur_a] += 4 - choi
        elif choi > 4:
            dict_survey[sur_b] += choi - 4
        
    for l in li:
        a, b = l[0], l[1]
        if dict_survey[a] < dict_survey[b]:
            answer += b
        else:
            answer += a
    return answer