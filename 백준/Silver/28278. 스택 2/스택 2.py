import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def solve():
    n = int(input())
    st = deque([])
    for i in range(n):
        cmd =list(map(int, input().split()))
        if cmd[0] == 1:
            st.append(cmd[1])
        elif cmd[0] == 2:
            if st:
                print(st.pop())
            else:
                print(-1)
        elif cmd[0] == 3:
            print(len(st))
        elif cmd[0] == 4:
            print(0 if st else 1)
        else:
            if st:
                top = st.pop()
                print(top)
                st.append(top)
            else:
                print(-1)


solve()