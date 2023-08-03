import sys
from collections import deque

input = sys.stdin.readline
ans = 0
for i in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(11)]
    chk = [0] * 11
    ans = 0

    def b_trc(player, sco):
        global ans
        if player >= 11:
           ans = max(ans, sco)
           return

        for i in range(11):
            val = arr[player][i]
            if val == 0 or chk[i]:
                continue
            else:
                chk[i] = 1
                b_trc(player + 1, sco + val)
                chk[i] = 0


    b_trc(0, 0)
    print(ans)
