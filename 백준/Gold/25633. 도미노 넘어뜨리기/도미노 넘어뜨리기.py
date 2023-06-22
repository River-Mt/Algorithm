import sys


def solve():
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    ords = [i for i in range(n)]
    answer = 0
    for i in range(0, n):
        cnt = 1
        p_sum = arr[i]
        for j in range(i + 1, n):
            if arr[j] <= p_sum:
                p_sum += arr[j]
                cnt += 1
        answer = max(answer, cnt)

    print(answer)


solve()