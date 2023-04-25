import sys

n = int(sys.stdin.readline().rstrip())
list = list(map(int, input().split()))
ans = 0
tmp = []
chk = [0 for i in range(n)]


def b_trc(loc):
    global ans
    if loc >= n:
        sum = 0
        for i in range(n - 1):
            sum += abs(list[tmp[i]] - list[tmp[i + 1]])
        ans = max(sum, ans)
        return

    for i in range(n):
        if chk[i] == 0:
            chk[i] = 1
            tmp.append(i)
            b_trc(loc + 1)
            tmp.pop()
            chk[i] = 0


b_trc(0)
print(ans)
