import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

sorted_arr = sorted(arr, reverse=True)

for num in sorted_arr:
    print(num)
    