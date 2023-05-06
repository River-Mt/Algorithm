def solution(my_string):
    answer = [0] * 52

    for ch in my_string:
        if ch.islower():
            idx = ord(ch) - ord('a') + 26
        else:
            idx = ord(ch) - ord('A')
        answer[idx] += 1

    return answer