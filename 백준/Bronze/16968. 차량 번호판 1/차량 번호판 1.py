import sys
input = sys.stdin.readline


def solve():
    s = list(input().rstrip())
    idx = 0
    c = 26
    d = 10
    ans = 1

    while idx < len(s):
        same = 0
        cur = s[idx]
        while idx < len(s) and cur == s[idx]:
            same += 1
            idx += 1
        for i in range(0, same):
            if cur == 'c':
                if i == 0:
                    ans *= c
                else:
                    ans *= (c - 1)
            else:
                if i == 0:
                    ans *= d
                else:
                    ans *= (d - 1)

    print(ans)


solve()
