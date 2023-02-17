def solution(string):
    cnt_convert = 0
    cnt_zero = 0
    while True:
        cnt_convert += 1
        temp = string.count('1')
        cnt_zero += string.count('0')
        if temp == 1:
            answer = [cnt_convert, cnt_zero]
            return answer
        else:
            string = str(bin(temp))[2:]