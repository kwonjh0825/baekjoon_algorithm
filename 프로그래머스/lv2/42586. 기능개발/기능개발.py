from collections import deque

def solution(progress, speeds):
    answer = []
    days = deque()
    for i in range(len(progress)):
        temp = progress[i]
        day = 0
        while temp < 100:
            temp += speeds[i]
            day += 1
        days.append(day)
    
    while days:
        temp = days.popleft()
        cnt = 1
        for day in list(days):
            if temp < day:
                break
            else:
                cnt += 1
                days.remove(day)
        answer.append(cnt)
    return answer