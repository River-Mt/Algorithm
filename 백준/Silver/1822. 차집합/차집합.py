import sys


def get_input():
    return sys.stdin.readline().split()


a, b = map(int, get_input())

A = set(list(map(int, get_input())))
B = set(list(map(int, get_input())))

diff_set = sorted(A.difference(B))

if len(diff_set) == 0:
    print(0)
else:
    print(len(diff_set))
    print(*diff_set)
