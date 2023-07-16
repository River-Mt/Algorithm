import sys
from collections import deque
input = sys.stdin.readline


def solve():
    n = int(input().rstrip())

    def chk_message(s):
        dic = {}
        idx = 0
        x = len(s)
        while idx < x - 1:
            ch = s[idx]
            dic[ch] = dic.get(ch, 0) + 1
            if dic[ch] % 3 == 0:
                if ch != s[idx + 1]:
                    return "FAKE"
                else:
                    idx += 1
            idx += 1

        return "OK"

    for i in range(n):
        s = list(input())
        print(chk_message(s))

solve()
