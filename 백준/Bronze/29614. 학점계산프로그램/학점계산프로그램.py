import heapq
import sys

input = sys.stdin.readline


def solve():
    s = input()
    n = len(s)
    grade = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}
    idx = 0
    score_sum = 0
    subject = 0
    while idx < n - 1:
        if s[idx + 1] == "+":
            score_sum += grade[s[idx] + s[idx + 1]]
            idx += 2
        else:
            score_sum += grade[s[idx]]
            idx += 1
        subject += 1
    print(f'{(score_sum / subject):.5f}')


solve()
