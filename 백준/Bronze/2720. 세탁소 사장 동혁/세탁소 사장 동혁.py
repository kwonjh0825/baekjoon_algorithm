T = int(input())
for _ in range(T):
    cnt = []
    dollar = int(input())
    cnt.append(dollar//25)
    dollar = dollar % 25

    cnt.append(dollar//10)
    dollar = dollar % 10

    cnt.append(dollar//5)
    dollar = dollar % 5

    cnt.append(dollar)
    print(*cnt)