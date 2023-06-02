import sys
from itertools import permutations
A, B = sys.stdin.readline().split()
ans = -1

for perm in [''.join(item) for item in list(permutations(A))]:
    if perm[0] != '0' and int(perm) < int(B):
        ans = max(ans, int(perm))

print(ans)

