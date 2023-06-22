import sys

arr = sys.stdin.readline().rstrip().split('.')
answer = ''
if len(arr) == 0:
    print(-1)
    exit(0)

for s in arr:
    len_s = len(s)

    if s == '.':
        answer += '.'
        continue

    tmp = len_s // 4
    mod = len_s % 4

    if mod % 2:
        print(-1)
        exit(0)

    for i in range(tmp):
        answer += 'AAAA'

    for i in range(mod // 2):
        answer += 'BB'

    answer += '.'

print(answer[:len(answer)-1])

