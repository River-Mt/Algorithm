import sys
from collections import deque
input = sys.stdin.readline


def solve():
    n = 20
    point_sum = 0
    arr = {}
    dic = {"A+": 4.5,
           "A0": 4.0,
           "B+": 3.5,
           "B0": 3.0,
           "C+": 2.5,
           "C0": 2.0,
           "D+": 1.5,
           "D0": 1.0,
           "F": 0.0,
           "P": 0.0
           }
    ans = 0.0
    for i in range(n):
        subject, point, grade = input().split()
        point = float(point)
        if grade == 'P':
            continue
        point_sum += point
        ans = ans + (dic[grade] * point)

    if point_sum == 0:
        print(f'{0:0.6f}')
    else:
        print(f'{ans / point_sum:0.6f}')

solve()
