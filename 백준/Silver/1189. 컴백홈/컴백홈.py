import sys
input = sys.stdin.readline

def solution():
    r, c, k = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(r)]
    chk = [[0] * c for _ in range(r)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    ans = 0
    chk[r - 1][0] = 1

    def b_trc(cur_r, cur_c, cnt):
        if cnt == k:
            if cur_r == 0 and cur_c == c - 1:
                return 1
            else:
                return 0
        elif cnt > k:
            return 0
        ret = 0

        for i in range(4):
            nr, nc = cur_r + dr[i], cur_c + dc[i]
            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue
            if chk[nr][nc] or arr[nr][nc] == 'T':
                continue
            chk[nr][nc] = 1
            ret += b_trc(nr, nc, cnt + 1)
            chk[nr][nc] = 0

        return ret

    return b_trc(r-1, 0, 1)


print(solution())
