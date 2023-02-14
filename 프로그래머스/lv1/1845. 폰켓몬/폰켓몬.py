def solution(nums):
    answer = 0
    N = len(nums) // 2
    set_nums = set(nums)
    if len(set_nums) < N:
        return len(set_nums)
    else:
        return N
