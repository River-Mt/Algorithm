import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def solve():
    s = input().rstrip()
    target = input().rstrip()
    n = len(s)
    dic = {}

    def recur(word):
        x = len(word)
        if x == n:
            if word == s:
                print(1)
                exit(0)
            return
        if word[x-1] == 'A':
            tmp = word[:x-1]
            recur(tmp)

        if word[0] == 'B':
            tmp = word[::-1]
            recur(tmp[:x-1])
    recur(target)
    print(0)


solve()
