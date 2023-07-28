import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def solve():
    s = str(input().rstrip())
    target = str(input().rstrip())
    n = len(s)
    dic = {}
    
    def recur(word):
        x = len(word)
        if x == n:
            if word == s:
                print(1)
                exit(0)
            return

        st, ed = word[0], word[x-1]

        if ed == 'A' and not dic.get(word[:x-1]):
            dic[word[:x-1]] = 1
            recur(word[:x-1])

        if st == 'B' and not dic.get(word[::-1][:x-1]):
            dic[word[::-1][:x-1]] = 1
            recur(word[::-1][:x-1])

    recur(target)
    print(0)


solve()
