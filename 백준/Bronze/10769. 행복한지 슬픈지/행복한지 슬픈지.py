string = input().split(':')

cnt_happy = 0
cnt_sad = 0

for s in string:
    if '-(' in s:
        cnt_sad += 1
    elif '-)' in s:
        cnt_happy += 1

if not cnt_happy and not cnt_sad:
    print('none')
elif cnt_happy > cnt_sad:
    print('happy')
elif cnt_happy < cnt_sad:
    print('sad')
else:
    print('unsure')