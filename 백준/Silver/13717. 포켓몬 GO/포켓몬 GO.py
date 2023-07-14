import sys
input = sys.stdin.readline


def solve():
    n = int(input().rstrip())
    dic = {}
    pokemon = ""
    ans = [0, ""]
    cnt = 0
    for i in range(2 * n):
        p = 0
        k = 0
        if i % 2 == 0:
            pokemon = input().rstrip()
            dic[pokemon] = 0
            continue
        else:
            p, k = map(int, input().split())
            while k >= p:
                k = k - p + 2
                dic[pokemon] += 1
                cnt += 1
            if dic[pokemon] > ans[0]:
                ans[0] = dic[pokemon]
                ans[1] = pokemon

    print(cnt)
    print(ans[1])
    return


solve()