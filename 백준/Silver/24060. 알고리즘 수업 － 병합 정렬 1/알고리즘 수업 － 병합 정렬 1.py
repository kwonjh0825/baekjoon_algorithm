import sys

def merge_sort(li):
    if len(li) == 1:
        return li
    
    mid = (len(li) + 1)// 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
        
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            result.append(right[j])
            ans.append(right[j])
            j += 1
        
    while i < len(left):
        result.append(left[i])
        ans.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        ans.append(right[j])
        j += 1
    return result

a, k = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

ans = []
merge_sort(num_list)

if len(ans) < k:
    print(-1)
else:
    print(ans[k-1])