w_score = sum(sorted([int(input()) for _ in range(10)], reverse=True)[:3])
k_score = sum(sorted([int(input()) for _ in range(10)], reverse=True)[:3])
print(w_score, k_score)