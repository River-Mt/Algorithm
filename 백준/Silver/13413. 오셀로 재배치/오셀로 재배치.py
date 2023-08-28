import sys

input = sys.stdin.readline


def do_each_case(n):
    cur_state = list(input().rstrip())
    target_state = list(input().rstrip())
    w_cnt = 0
    b_cnt = 0

    for i in range(n):
        if cur_state[i] != target_state[i]:
            if cur_state[i] == 'W':
                w_cnt += 1
            else:
                b_cnt += 1

    return max(w_cnt, b_cnt)


def solve():
    tc = int(input())
    for i in range(tc):
        n = int(input())
        print(do_each_case(n))


solve()
