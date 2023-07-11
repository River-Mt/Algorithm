import sys
input = sys.stdin.readline

shape1 = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)]
]

shape2 = [
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
]

shape3 = [
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (0, 1)]
]

shape4 = [
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (-1, 1), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)]
]

shape5 = [
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

shapes = [shape1, shape2, shape3, shape4, shape5]

def is_over(r, c, n):
    if r < 0 or c < 0 or r >= n or c >= n:
        return True
    else:
        return False


def get_shape(arr, r, c):
    ret = -4000000

    for shape in shapes:
        for direction in shape:
            tmp = 0
            for (dr, dc) in direction:
                nr = r + dr
                nc = c + dc
                if is_over(nr, nc, n):
                    tmp = -4000000
                    break
                tmp += arr[nr][nc]
            ret = max(ret, tmp)
    return ret


def get_max(arr, n):
    ret = -4000000
    for i in range(n):
        for j in range(n):
            ret = max(ret, get_shape(arr, i, j))
    return ret


idx = 1

while True:
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'{idx}. {get_max(arr, n)}')
    idx += 1


