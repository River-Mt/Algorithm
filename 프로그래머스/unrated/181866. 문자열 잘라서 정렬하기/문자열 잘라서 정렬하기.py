def solution(myString):
    answer = sorted([(substring) for substring in myString.strip("x").split("x") if substring])
    return answer