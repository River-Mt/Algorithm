import sys

input = sys.stdin.readline
import collections


N, Q = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(2 ** N)]
L_list = list(map(int, input().split()))


def rotate(i, j, L):
    sub_MAP = []
    for ii in range(i, i + 2 ** L):
        sub_MAP.append(MAP[ii][j:j + 2 ** L])

    rotated = list(zip(*sub_MAP[::-1]))

    for ii in range(2 ** L):
        MAP[ii + i][j:j + 2 ** L] = rotated[ii]


def melt(MAP):
    tMAP = [line[:] for line in MAP]

    move = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    for x in range(len(MAP)):
        for y in range(len(MAP[0])):
            cnt = 0
            for tx, ty in move:
                nx = tx + x
                ny = ty + y

                if 0 <= nx < len(MAP) and 0 <= ny < len(MAP[0]) and MAP[nx][ny] > 0:
                    cnt += 1

                if cnt >= 3:
                    break

            else:
                tMAP[x][y] = MAP[x][y] - 1

    return tMAP


def firestorm(MAP, L):
    for i in range(0, len(MAP), 2 ** L):
        for j in range(0, len(MAP[0]), 2 ** L):
            if L != 0:
                rotate(i, j, L)

    MAP = melt(MAP)

    return MAP


def bfs(MAP, sx, sy):
    move = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    q = collections.deque()
    q.append((sx, sy))
    total = MAP[sx][sy]
    MAP[sx][sy] = -1
    cnt = 1

    while q:
        cx, cy = q.popleft()

        for tx, ty in move:
            nx = tx + cx
            ny = ty + cy

            if 0 <= nx < len(MAP) and 0 <= ny < len(MAP[0]) and MAP[nx][ny] > 0:
                q.append((nx, ny))
                total += MAP[nx][ny]
                MAP[nx][ny] = -1
                cnt += 1

    return total, cnt


def find_dummy(MAP):
    total = 0
    max_island = 0

    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            if MAP[i][j] > 0:
                total_ice, island_cnt = bfs(MAP, i, j)
                max_island = max(max_island, island_cnt)
                total += total_ice

    return total, max_island


for i in range(Q):
    MAP = firestorm(MAP, L_list[i])

print(*find_dummy(MAP))