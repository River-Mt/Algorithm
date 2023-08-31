import sys

input = sys.stdin.readline


def get_dic():
    dic = {}
    alp = 0
    for i in range(10, 36):
        dic[chr(ord('A') + alp)] = i
        alp += 1
    return dic


def convert(n, b, dic):
    ret = 0
    n_len = len(n)
    for i in range(n_len):
        if '0' <= n[i] <= '9':
            ret += (b ** (n_len - i - 1)) * int(n[i])
        else:
            ret += (b ** (n_len - i - 1)) * dic[n[i]]
    return ret


def solve():
    n, b = input().split()
    n = list(n)
    b = int(b)
    return convert(n, b, get_dic())


print(solve())
