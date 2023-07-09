import sys

n, m, l = map(int, sys.stdin.readline().split())
s = []
for i in range(m):
    s.append(int(sys.stdin.readline().rstrip()))

s += [l]

def b_search(q, ans):
    left = 1
    right = l
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        tmp = 0
        for x in s:
            if x - tmp >= mid:
                tmp = x
                cnt += 1
        if cnt > q:
            left = mid + 1
            ans = max(ans, mid)
        else:
            right = mid - 1

    return ans


for i in range(n):
    q = int(sys.stdin.readline().rstrip())
    print(b_search(q, 0))


