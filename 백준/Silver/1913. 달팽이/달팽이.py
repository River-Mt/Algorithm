import sys
input = sys.stdin.readline

n = int(input())
HALF = n // 2
target = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
sr, sc = HALF, HALF
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = 0
idx = 1
tr, tc = 0, 0

for k in range(1, n):
    for t in range(2):
        for i in range(k):
            if idx == target:
                tr, tc = sr, sc
            arr[sr][sc] = idx
            idx += 1
            sr += dr[d]
            sc += dc[d]
        d = (d+1) % 4

for i in range(n):
    if idx == target:
        tr, tc = sr, sc
    arr[sr][sc] = idx
    idx += 1
    sr += dr[d]
    sc += dc[d]

for row in arr:
    print(*row)

print(tr+1, tc+1)





