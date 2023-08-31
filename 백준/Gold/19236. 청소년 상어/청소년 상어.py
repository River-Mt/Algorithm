import copy
import sys

input = sys.stdin.readline
r, c = 4, 4
# directions: counter-clock
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
ans = 0


def get_state():
    state = []

    for i in range(r):
        rows = list(map(int, input().split()))
        tmp = []
        j = 0
        while j < r * 2:
            tmp.append([rows[j], rows[j + 1] - 1])
            j += 2
        state.append(tmp)

    return state


def is_over(nr, nc):
    return nr < 0 or nc < 0 or nr >= r or nc >= c


def is_shark_loc(nr, nc, sr, sc):
    return nr == sr and nc == sc


def is_exist_fist(nr, nc, state):
    return state[nr][nc][0] > 0


def can_not_fish_move(nr, nc, sr, sc):
    return is_over(nr, nc) or is_shark_loc(nr, nc, sr, sc)


def can_not_shark_move(nr, nc, state):
    return is_over(nr, nc) or not is_exist_fist(nr, nc, state)


def swap(a, b):
    return b, a


def find_pish(fish, state):
    for i in range(r):
        for j in range(c):
            if state[i][j][0] == fish:
                return i, j
    return -1, -1


def fish_move(sr, sc, state):
    for fish_num in range(1, 17):
        fr, fc = find_pish(fish_num, state)

        if fr == -1 and fc == -1:
            continue

        fd = state[fr][fc][1]

        for d in range(8):
            nfd = (fd + d) % 8
            nfr, nfc = fr + dr[nfd], fc + dc[nfd]

            if can_not_fish_move(nfr, nfc, sr, sc):
                continue

            state[fr][fc][1] = nfd
            state[fr][fc], state[nfr][nfc] = state[nfr][nfc], state[fr][fc]

            break

    return


def shark_move(sr, sc, state, val):
    global ans
    state[sr][sc][0] = 0
    ans = max(ans, val)

    fish_move(sr, sc, state)

    sd = state[sr][sc][1]

    for d in range(1, 5):
        nsr, nsc = sr + dr[sd] * d, sc + dc[sd] * d

        if can_not_shark_move(nsr, nsc, state):
            continue

        shark_move(nsr, nsc, copy.deepcopy(state), val + state[nsr][nsc][0])

    return


def solve():
    state = get_state()
    shark_move(0, 0, state, state[0][0][0])
    return


solve()
print(ans)
