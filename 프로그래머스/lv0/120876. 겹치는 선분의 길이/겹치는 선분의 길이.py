def solution(lines):
    answer = 0
    lineSets = [set(range(min(x), max(x))) for x in lines]
    answer = len(lineSets[0] & lineSets[1] | lineSets[1] & lineSets[2] | lineSets[2] & lineSets[0]) 
    return answer