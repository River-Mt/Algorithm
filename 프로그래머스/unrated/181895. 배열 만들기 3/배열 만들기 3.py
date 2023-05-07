def solution(arr, intervals):
    answer = []
    for interval in intervals:
        a = interval[0]
        b = interval[1]
        answer.extend(arr[a:b+1])
    return answer