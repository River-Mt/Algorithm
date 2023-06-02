import sys


def read_input(): return sys.stdin.readline()


def binary_search(target_num, numbers, end):
    left = 0
    right = end - 1
    while left <= right:
        mid = (left + right) // 2
        cur = numbers[mid]
        if cur == target_num:
            return 1
        elif cur < target_num:
            left = mid + 1
        else:
            right = mid - 1
    return 0


n = int(read_input())
arr = list(map(int, read_input().split()))
sorted_arr = sorted(arr)
m = int(read_input())
targets = list(map(int, read_input().split()))

for target in targets:
    print(binary_search(target, sorted_arr, n))
