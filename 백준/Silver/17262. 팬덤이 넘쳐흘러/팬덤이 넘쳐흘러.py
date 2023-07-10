import sys
input = sys.stdin.readline

n = int(input())
starts = []
ends = []

for i in range(n):
    s, e = map(int, input().split())
    starts.append(s)
    ends.append(e)

starts = sorted(starts, reverse=True)
ends = sorted(ends)
ans = starts[0] - ends[0]

print(ans if ans > 0 else 0)

