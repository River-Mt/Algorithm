import bisect

def solution(array, height):
    return (len(array) - bisect.bisect_right(sorted(array), height))
