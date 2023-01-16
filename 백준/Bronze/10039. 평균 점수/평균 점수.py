li = []
for _ in range(5):
    n = int(input())
    li.append(n) if n > 40 else li.append(40)
print(int(sum(li)/len(li)))