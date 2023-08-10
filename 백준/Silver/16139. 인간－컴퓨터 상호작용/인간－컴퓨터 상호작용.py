import sys

input = sys.stdin.readline


def get_alpha_ord(alp):
    return ord(alp) - ord('a')


s = input().rstrip()
q = int(input())
p_sum = [[0 for _ in range(27)] for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    alp_ord = get_alpha_ord(s[i - 1])

    for j in range(27):
        p_sum[i][j] = p_sum[i-1][j]

    p_sum[i][alp_ord] += 1


for i in range(q):
    ch, l, r = input().split()
    alp_ord = ord(ch) - ord('a')
    l, r = int(l) + 1, int(r) + 1
    print(p_sum[r][alp_ord] - p_sum[l - 1][alp_ord])
