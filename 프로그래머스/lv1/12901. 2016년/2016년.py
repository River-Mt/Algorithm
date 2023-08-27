def solution(a, b):
    answer = ''
    dates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    answer = sum(dates[:a-1])
    return (day[(answer + b) % 7])
