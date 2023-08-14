import sys
import bisect

input = sys.stdin.readline
n = int(input())
numbers = []

for i in range(n):
    numbers.append(input())

m = len(numbers[0])

for i in range(m):
    dic = {}
    for number in numbers:
        sub = "".join(number[i:])
        if dic.get(sub):
            print(m - i)
            exit(0)

        dic[sub] = 1
