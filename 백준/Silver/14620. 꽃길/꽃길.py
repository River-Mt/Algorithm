import sys

n = int(sys.stdin.readline().rstrip())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 1e9
dr = [0, 0, 0, -1, 1]
dc = [0, -1, 1, 0, 0]


def is_overlap(r, c, chk):
    for d in range(5):
        if (r + dr[d], c + dc[d]) in chk:
            return True
    return False


def dfs(chk, cost_sum):
    global answer

    if answer <= cost_sum:
        return

    if len(chk) >= 15:
        answer = min(answer, cost_sum)

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if not is_overlap(i, j, chk):
                tmp = []
                tmp_sum = 0
                for d in range(5):
                    ni, nj = i + dr[d], j + dc[d]
                    tmp.append((ni, nj))
                    tmp_sum += costs[ni][nj]
                dfs(chk + tmp, cost_sum + tmp_sum)


dfs([], 0)
print(answer)
