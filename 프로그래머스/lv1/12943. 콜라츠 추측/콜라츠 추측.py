def go(num, cnt):
    if num == 1:
        return cnt

    if cnt >= 500:
        return -1

    if num % 2 == 0:
        return go(int(num // 2), cnt + 1)

    else:
        return go((num * 3) + 1, cnt + 1)


def solution(num):
    if num == 1:
        return 0
    return go(num, 0)


print(solution(6))
