import sys


def solve():
    n = int(sys.stdin.readline().rstrip())
    limits = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    m = int(sys.stdin.readline().rstrip())
    box_weights = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    if box_weights[0] > limits[0]:
        return -1

    cnt = 0

    while True:
        if not box_weights:
            break

        for i in range(n):
            for j in range(len(box_weights)):
                if box_weights[j] <= limits[i]:
                    del box_weights[j]
                    break
        cnt += 1

    return cnt


print(solve())

