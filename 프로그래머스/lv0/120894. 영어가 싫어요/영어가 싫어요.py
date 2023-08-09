import re
def solution(numbers):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    strs = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = numbers
    
    for i in range(10):
        answer = answer.replace(strs[i], nums[i])

    
    return int(answer)