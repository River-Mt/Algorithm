import sys

input = sys.stdin.readline

s = list(input().rstrip())
n = len(s)
ans = "z" * 51

for i in range(1, n):
    for j in range(i+1, n):
        ans = min(ans, ("".join(s[:i])[::-1]) + ("".join(s[i:j])[::-1]) + ("".join(s[j:])[::-1]))

print(ans)
