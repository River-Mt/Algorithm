import sys
from itertools import permutations

x = list(sys.stdin.readline().rstrip())
ans = 0
combs = list(permutations(x, len(x)))
arr = []

for comb in combs:
    arr.append("".join(comb))

for s in sorted(arr):
    if int(s) > int("".join(x)):
        print(s)
        exit(0)

print(0)