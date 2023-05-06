from itertools import permutations
import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
perms = map(list, permutations(arr))

for perm in perms:
    weights = 500
    flag = True
    for w in perm:
        weights += w - k
        if weights < 500:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
