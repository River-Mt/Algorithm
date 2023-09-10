import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

s = list(input().rstrip())
n = len(s)
chk = [0 for _ in range(n)]
dic = {}


def dfs(state, idx):
    if idx == n:
        if dic.get(state):
            return 0
        dic[state] = 1

        return 1

    ret = 0

    for i in range(n):
        if chk[i] == 0:
            if state and state[idx - 1] == s[i]:
                continue

            chk[i] = 1
            ret += dfs(state + s[i], idx + 1)
            chk[i] = 0

    return ret


print(dfs("", 0))
