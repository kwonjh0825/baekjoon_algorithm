dial = {'ABC': 3, 'DEF': 4, 'GHI': 5 , 'JKL': 6, 'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
string = input()
time = 0
for s in string:
    for j in dial:
        if s in j:
            time += dial.get(j)
            break

print(time)