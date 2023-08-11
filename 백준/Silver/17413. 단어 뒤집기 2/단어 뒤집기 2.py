import sys

input = sys.stdin.readline

s = list(input().rstrip())
n = len(s)
idx = 0
output = ""

while idx < n:
    if s[idx] == '<':
        while True:
            output += s[idx]
            if s[idx] == '>':
                idx += 1
                break
            idx += 1


    elif s[idx] == ' ':
        output += ' '
        idx += 1

    else:
        tmp = ""
        while True:
            if idx >= n or s[idx] == '<' or s[idx] == ' ':
                break
            tmp += s[idx]
            idx += 1
        output += tmp[::-1]

print(output)
