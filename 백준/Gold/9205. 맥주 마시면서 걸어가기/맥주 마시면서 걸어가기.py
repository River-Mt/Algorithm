import sys
from collections import deque
input = sys.stdin.readline


def solve():
    t = int(input().rstrip())

    def get_dist(r1, c1, r2, c2):
        return abs(r1 - r2) + abs(c1 - c2)

    def can_go(r1, c1, r2, c2):
        if get_dist(r1, c1, r2, c2) <= 1000:
            return True
        else:
            return False

    def bfs(n):
        q = deque([])
        chk = [[hr, hc]]
        q.append([hr, hc])

        while q:
            cur = q.popleft()
            r, c = cur[0], cur[1]
            # 페스티벌에 도달할 수 있는지 확인
            if can_go(pr, pc, r, c):
                return "happy"

            for i in range(len(conv)):
                if conv[i] in chk:
                    continue
                nr, nc = conv[i]

                if can_go(r, c, nr, nc):
                    q.append([nr, nc])
                    chk.append([nr, nc])

        return "sad"

    for i in range(t):
        n = int(input().rstrip())
        conv = []
        # home loc
        hr, hc = map(int, input().split())
        # conv loc
        for _ in range(n):
            cr, cc = map(int, input().split())
            conv.append([cr, cc])
        # penta fest loc
        pr, pc = map(int, input().split())

        print(bfs(n))


solve()
