from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    remains = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    if len(remains) == 1:
        return 1

    prev = remains[0]
    cnt = 1
    for i in range(1, len(remains)):
        r = remains[i]
        if prev >= r:
            cnt += 1
            continue
        answer.append(cnt)
        cnt = 1
        prev = remains[i]

    answer.append(cnt)

    return answer


