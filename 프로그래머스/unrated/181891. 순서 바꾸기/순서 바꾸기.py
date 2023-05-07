def solution(num_list, n):
    answer = []
    answer.extend(num_list[n:] + num_list[:n])
    return answer