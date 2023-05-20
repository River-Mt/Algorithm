import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
sorted_arr = sorted(arr)

print(sorted_arr[(n-1) // 2])
