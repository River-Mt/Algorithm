import math

n = int(input())
arr = []
ans = 0

for i in range(n):
    arr.append(list(map(int, input().split())))

sr = sc = n // 2

# L D R U

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

chk = [
    [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [0, -2], [-2, 0], [2, 0]],
    [[-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 1], [2, 0], [0, -2], [0, 2]],
    [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [0, 2], [-2, 0], [2, 0]],
    [[-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 1], [-2, 0], [0, -2], [0, 2]]
]

rates = [
    [0.1, 0.07, 0.01, 0.1, 0.07, 0.01, 0.05, 0.02, 0.02],
    [0.01, 0.01, 0.07, 0.07, 0.1, 0.1, 0.05, 0.02, 0.02],
    [0.01, 0.07, 0.1, 0.01, 0.07, 0.1, 0.05, 0.02, 0.02],
    [0.1, 0.1, 0.07, 0.07, 0.01, 0.01, 0.05, 0.02, 0.02]
]


def is_over(r, c):
    if 0 <= r < n and 0 <= c < n:
        return False
    else:
        return True


def spread_dust(r, c, d):
    global ans
    tmp = 0
    for i in range(9):
        nr, nc = r + chk[d][i][0], c + chk[d][i][1]
        add = math.floor(arr[r][c] * rates[d][i])

        tmp += add

        if is_over(nr, nc):
            ans += add
        else:
            arr[nr][nc] += add

    if not is_over(r + dr[d], c + dc[d]):
        arr[r + dr[d]][c + dc[d]] += (arr[r][c] - tmp)

    else:
        ans += (arr[r][c] - tmp)

    arr[r][c] = 0


def move():
    d = 0
    r = sr
    c = sc

    for i in range(1, n):
        for j in range(2):
            for k in range(i):
                r += dr[d]
                c += dc[d]
                spread_dust(r, c, d)

            d = (d + 1) % 4

    for i in range(n - 1):
        r += dr[d]
        c += dc[d]
        spread_dust(r, c, d)


move()

print(ans)
