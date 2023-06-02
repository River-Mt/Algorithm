import sys

n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.append(0)
arr = sorted(arr)
p_sum = [0] * (n+1)

for i in range(1, n + 1):
    p_sum[i] = p_sum[i - 1] + arr[i]

for i in range(q):
    l, r = map(int, sys.stdin.readline().split())
    print(p_sum[r] - p_sum[l - 1])

