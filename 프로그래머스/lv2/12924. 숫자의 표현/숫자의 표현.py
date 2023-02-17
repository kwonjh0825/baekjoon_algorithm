def solution(n):
    answer = 0
    for i in range(1, (n//2) + 1):
        temp = 0
        while True:
            temp += i
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
            i += 1

    return answer + 1
