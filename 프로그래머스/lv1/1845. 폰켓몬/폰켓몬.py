def solution(nums):
    answer = 0
    dict = {}
    n = len(nums)
    for num in nums:
        dict[num] = dict.get(num, 0) + 1
    
    if n//2 >= len(dict):
        answer = len(dict)
    else:
        answer = n//2

    return answer