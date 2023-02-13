import sys

input = sys.stdin.readline

N, K = map(int, input().split())
li = list(map(int, input().split()))

temp = sum(li[:K])
prefix_sum = [temp]
for i in range(len(li)-K):
    temp = temp - li[i] + li[i+K]
    prefix_sum.append(temp)
print(max(prefix_sum))