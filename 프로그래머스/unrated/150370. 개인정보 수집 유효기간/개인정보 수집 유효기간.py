def solution(today, terms, privacies):
    ans = []
    dict_term = dict()
    t_year, t_month, t_day = map(int, today.split('.'))
    for t in terms:
        a, b = t.split()
        dict_term[a] = int(b)
    for i, p in enumerate(privacies):
        date, term = p.split()
        year, month, day = map(int, date.split('.'))
        day -= 1
        month += dict_term[term]
        if month > 12:
            year += month // 12
            month = month % 12
        if day < 1:
            day += 28
            month -= 1
        if month < 1:
            year -= 1
            month += 12
        
        if t_year > year:
            ans.append(i+1)
        elif t_year == year and t_month > month:
            ans.append(i+1)
        elif t_year == year and t_month == month and t_day > day:
            ans.append(i+1)
    return ans