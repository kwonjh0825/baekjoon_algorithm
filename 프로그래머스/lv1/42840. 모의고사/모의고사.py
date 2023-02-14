def solution(answers):
    answer = []
    ans_1 = [1,2,3,4,5]
    ans_2 = [2,1,2,3,2,4,2,5]
    ans_3 = [3,3,1,1,2,2,4,4,5,5]
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    
    for i, ans in enumerate(answers):
        if ans_1[i%5] == ans:
            cnt_1 += 1
        if ans_2[i%8] == ans:
            cnt_2 += 1
        if ans_3[i%10] == ans:
            cnt_3 += 1
    max_cnt = max(cnt_1, cnt_2, cnt_3)
    if max_cnt == cnt_1:
        answer.append(1)
    if max_cnt == cnt_2:
        answer.append(2)
    if max_cnt == cnt_3:
        answer.append(3)
    return answer