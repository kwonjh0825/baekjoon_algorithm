def solution(clothes:list):
    answer = 1
    dict_clothes = {}
    for c in clothes:
        a, b = c[0], c[1]
        if b not in dict_clothes.keys():
            dict_clothes[b] = [a]
        else:
            dict_clothes[b].append(a)
    for value in dict_clothes.values():
        answer = answer * (len(value) + 1)
    return answer - 1