import sys


def isInvalid(a, b, c):
    if a >= b + c:
        return True

    return False


while True:
    tri = list(map(int, sys.stdin.readline().split()))
    tri.sort()
    c, b, a = tri

    if a + b + c == 0:
        break

    if isInvalid(a, b, c):
        print("Invalid")
        continue

    count = {}

    for line in tri:
        count[line] = count.get(line, 0) + 1

    print("Equilateral" if len(count) == 1 else "Isosceles" if len(count) == 2 else "Scalene")
