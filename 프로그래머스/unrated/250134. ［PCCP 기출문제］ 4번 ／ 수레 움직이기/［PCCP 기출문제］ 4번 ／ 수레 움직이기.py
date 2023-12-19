import sys

sys.setrecursionlimit(10 ** 8)


def solution(maze):
    n = len(maze)
    m = len(maze[0])
    moving_red = [0, 0]
    target_red = [0, 0]
    moving_blue = [0, 0]
    target_blue = [0, 0]
    inf = 10000000
    answer = inf
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    red_visit = set()
    blue_visit = set()

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                moving_red = [i, j]
            elif maze[i][j] == 2:
                moving_blue = [i, j]
            elif maze[i][j] == 3:
                target_red = [i, j]
            elif maze[i][j] == 4:
                target_blue = [i, j]

    def in_range(curr):
        return 0 <= curr[0] < n and 0 <= curr[1] < m

    def go(red, blue, turn):
        nonlocal answer
        if red == target_red and blue == target_blue:
            answer = min(answer, turn)
            return

        elif red == target_red:
            for bd in range(4):
                nbr = blue[0] + dr[bd]
                nbc = blue[1] + dc[bd]
                if not in_range([nbr, nbc]):
                    continue
                if maze[nbr][nbc] == 5:
                    continue
                if (nbr, nbc) in blue_visit:
                    continue
                if [nbr, nbc] == red:
                    continue
                blue_visit.add((nbr, nbc))
                go(red, [nbr, nbc], turn + 1)
                blue_visit.remove((nbr, nbc))

        elif blue == target_blue:
            for rd in range(4):
                nrr = red[0] + dr[rd]
                nrc = red[1] + dc[rd]
                if not in_range([nrr, nrc]):
                    continue
                if maze[nrr][nrc] == 5:
                    continue
                if (nrr, nrc) in red_visit:
                    continue
                if [nrr, nrc] == blue:
                    continue
                red_visit.add((nrr, nrc))
                go([nrr, nrc], blue, turn + 1)
                red_visit.remove((nrr, nrc))

        else:
            for rd in range(4):
                nrr = red[0] + dr[rd]
                nrc = red[1] + dc[rd]
                if not in_range([nrr, nrc]):
                    continue
                if maze[nrr][nrc] == 5:
                    continue
                if (nrr, nrc) in red_visit:
                    continue

                for bd in range(4):
                    nbr = blue[0] + dr[bd]
                    nbc = blue[1] + dc[bd]
                    if not in_range([nbr, nbc]):
                        continue
                    if maze[nbr][nbc] == 5:
                        continue
                    if (nbr, nbc) in blue_visit:
                        continue
                    if [nbr, nbc] == red and [nrr, nrc] == blue:
                        continue
                    if [nrr, nrc] == [nbr, nbc]:
                        continue

                    blue_visit.add((nbr, nbc))
                    red_visit.add((nrr, nrc))
                    go([nrr, nrc], [nbr, nbc], turn + 1)
                    blue_visit.remove((nbr, nbc))
                    red_visit.remove((nrr, nrc))

    red_visit.add((moving_red[0], moving_red[1]))
    blue_visit.add((moving_blue[0], moving_blue[1]))

    go(moving_red, moving_blue, 0)

    return answer if answer != inf else 0
