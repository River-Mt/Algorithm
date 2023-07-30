import sys

input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    floors = []

    def rotate(org):
        return ["".join(list(reversed(elem))) for elem in zip(*org)]

    def count(li, sep):
        tmp = 0
        for r in li:
            for s in r.split(sep):
                if s != '':
                    tmp += 1
        return tmp

    for i in range(n):
        floors.append(str(input().rstrip()))

    print(count(floors, '|') + count(rotate(floors), '-'))


solve()
