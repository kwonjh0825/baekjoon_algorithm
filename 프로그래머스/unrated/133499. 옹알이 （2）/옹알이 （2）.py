def solution(babbling):
    answer = 0
    vib = ['aya', 'ye', 'woo', 'ma']
    for b in babbling:
        for v in vib:
            if v * 2 not in b:
                b = b.replace(v, ' ')
        if b.strip() == '':
            answer += 1
    return answer

