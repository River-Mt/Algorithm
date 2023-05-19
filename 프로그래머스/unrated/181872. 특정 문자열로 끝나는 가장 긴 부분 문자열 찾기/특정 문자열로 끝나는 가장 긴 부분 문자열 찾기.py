def solution(myString, pat):
    answer = ''
    revMy = myString[::-1]
    revPat = pat[::-1]
    idx = revMy.find(revPat)
    answer = myString[:len(myString) - idx]
    return answer