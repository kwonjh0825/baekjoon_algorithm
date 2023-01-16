N = int(input())
survey = [int(input()) for _ in range(N)]
ans = 0 if survey.count(1) > survey.count(0) else 1
print('Junhee is ' + (ans * 'not ') + 'cute!')