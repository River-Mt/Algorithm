import sys

h, w, n, m = map(int, sys.stdin.readline().split())

ans = ((h+n) // (n+1)) * ((w+m) // (m+1))

print(ans)
