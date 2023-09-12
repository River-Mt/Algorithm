import sys

input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())
idx = len(A) - 1
diff = 0
for a in A[::-1]:
    if a != B[idx]:
        diff += 1
    else:
        idx -= 1

if sorted(A) != sorted(B):
    print(-1)

else:
    print(diff)
