n, m = map(int, input().split())
chk = [0 for i in range(n + 1)]
ans = []


def b_trc(now):
    if len(ans) == m:
        print(*ans)
    for i in range(n):
        if chk[i + 1] != 1:
            chk[i + 1] = 1
            ans.append(i + 1)
            b_trc(i + 1)
            ans.pop()
            chk[i + 1] = 0


b_trc(1)
