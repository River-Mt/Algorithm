import sys

s = sys.stdin.readline().rstrip()
sfx = []
for i in range(len(s)):
    sfx.append(s[i:])

sfx.sort()

for x in sfx:
    print(x, end="\n")
