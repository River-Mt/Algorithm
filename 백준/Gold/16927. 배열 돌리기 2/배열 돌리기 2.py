n, m, r = map(int, input().split())
arr = []


def rotate(arr, sr, sc):
    tmp = arr[sr][sc]

    for i in range(sc, m - 1 - sc):
        arr[sr][i] = arr[sr][i + 1]

    for i in range(sr, n - 1 - sr):
        arr[i][m - 1 - sc] = arr[i + 1][m - 1 - sc]

    for i in range(m - 1 - sc, sc, -1):
        arr[n - sr - 1][i] = arr[n - sr - 1][i - 1]

    for i in range(n - 1 - sr, sr, -1):
        arr[i][sc] = arr[i - 1][sc]

    arr[sr + 1][sc] = tmp


for i in range(n):
    arr.append(list(map(int, input().split())))

x = min(n, m) // 2

for i in range(x):
    t = (n-2*i)*2 + ((m-2*i)-2) * 2
    for j in range(r % t):
        rotate(arr, i, i)

for row in arr:
    print(*row)
