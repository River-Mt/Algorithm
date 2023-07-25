import sys

input = sys.stdin.readline

def solve():
   n = int(input().rstrip())
   num = 666
   nth = 0

   while True:
        if '666' in str(num):
            nth += 1
        if nth == n:
            print(num)
            break
        num += 1


solve()
