import sys

input = sys.stdin.readline

l = int(input())
string = input().strip()
ans = 0
for i, s in enumerate(string):
    ans += (ord(s)-96) * 31**i
print(ans%1234567891)