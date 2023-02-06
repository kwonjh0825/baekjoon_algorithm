max_client = 0
now = 0
for _ in range(4):
    a, b = map(int, input().split())
    now -= a
    now += b
    max_client = max(max_client, now)
print(max_client)