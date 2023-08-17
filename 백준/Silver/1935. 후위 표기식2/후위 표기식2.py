import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def solve():
    n = int(input())
    formula = list(input().rstrip())
    exp = deque(list())
    operators = ['+', '/', '*', '-']
    ch_to_num = {}

    def is_alp(ch):
        return 'A' <= ch <= 'Z'

    def is_operator(op):
        return op in operators

    for i in range(n):
        ch_to_num[chr(ord('A') + i)] = input().rstrip()

    for i in range(len(formula)):
        ch = formula[i]
        if is_alp(ch):
            formula[i] = ch_to_num[ch]

    formula = deque(formula)

    while formula:
        cur = formula.popleft()

        if not is_operator(cur):
            exp.append(cur)

        else:
            back = exp.pop()
            front = exp.pop()
            exp.append(str(eval(front + cur + back)))

    return float(exp.popleft())


print(f'{solve():.2f}')
