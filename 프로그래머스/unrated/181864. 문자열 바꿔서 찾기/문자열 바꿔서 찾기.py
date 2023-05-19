def solution(myString, pat):
    replaced_string = myString.replace("A", "X").replace("B", "A").replace("X", "B")
    return int(pat in replaced_string)