import sys

n, m = map(int, sys.stdin.readline().split())
arr = sys.stdin.readline().split()
p_sum = [0] * (n + 1)
p_sum[1] = int(arr[0])

for i in range(2, n + 1):
    p_sum[i] = p_sum[i - 1] + int(arr[i - 1])

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(p_sum[e] - p_sum[s - 1])


