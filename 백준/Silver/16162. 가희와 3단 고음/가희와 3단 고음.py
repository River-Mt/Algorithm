import sys

input = sys.stdin.readline

n, a, d = map(int, input().split())
notes = list(map(int, input().split()))
cnt = 0

for note in notes:
    if note == a + (d * cnt):
        cnt += 1

print(cnt)
