from collections import deque

def solution(priorities, location):
    dq = deque([(i, num) for i, num in enumerate(priorities)])

    answer = 0

    while dq:
        cur = dq.popleft()
        if any(cur[1] < q[1] for q in dq): dq.append(cur)
        else:
            answer += 1
            if cur[0] == location: return answer