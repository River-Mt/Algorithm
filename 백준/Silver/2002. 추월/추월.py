import sys

input = sys.stdin.readline


def get_in_order(n):
    order = 1
    in_order = {}

    for i in range(n):
        car = input().rstrip()
        in_order[car] = order
        order += 1

    return in_order


def chk_out_car(n, in_order):
    cnt = 0
    out_cars = []

    for i in range(n):
        car = input().rstrip()
        out_cars.append(in_order[car])

    for i in range(n):
        for j in range(i + 1, n):
            if out_cars[i] > out_cars[j]:
                cnt += 1
                break

    return cnt


def solve():
    n = int(input())
    return chk_out_car(n, get_in_order(n))


print(solve())
