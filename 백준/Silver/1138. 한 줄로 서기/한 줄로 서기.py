import sys


n = int(sys.stdin.readline().rstrip())
line = list(map(int, sys.stdin.readline().split()))
ans = [0] * n

for i in range(n):
    tall = line[i]
    zeroCnt = -1
    for j in range(n):
        if ans[j] == 0:
            zeroCnt += 1

        if zeroCnt == tall:
            ans[j] = i + 1
            break

print(*ans)
