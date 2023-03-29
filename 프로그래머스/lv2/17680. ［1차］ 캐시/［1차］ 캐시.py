from collections import deque

def solution(cacheSize, cities):
    ans = 0
    li = deque()
    if cacheSize < 1:
        return len(cities) * 5
    else:
        for city in cities:
            city = city.lower()
            if city in li:
                li.remove(city)
                li.append(city)
                ans += 1
            elif len(li) < cacheSize:
                li.append(city)
                ans += 5
            else:
                li.popleft()
                li.append(city)
                ans += 5

        return ans