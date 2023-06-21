import bisect

def solution(array, n):
    answer = 0 
    arr = [(abs(num - n), num) for num in array] 
    return sorted(arr)[0][1]