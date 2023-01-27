input()
pro = 0
while True:
    string = input()
    if string == '문제':
        pro += 1
    elif string == '고무오리':
        if pro:
            pro -= 1
        else:
            pro += 2
    else:
        break
if pro:
    print('힝구')
else:
    print('고무오리야 사랑해')