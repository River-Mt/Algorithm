import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dq = deque()
for i in range(n):
    s = sys.stdin.readline().split()
    cmd = s[0]

    if cmd == 'push_front':
        dq.appendleft(s[1])
    elif cmd == 'push_back':
        dq.append(s[1])
    elif cmd == 'pop_front':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif cmd == 'pop_back':
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        if not len(dq):
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if not dq:
            print(-1)
        else:
            top = dq.popleft()
            print(top)
            dq.appendleft(top)
    elif cmd == 'back':
        if not dq:
            print(-1)
        else:
            top = dq.pop()
            print(top)
            dq.append(top)
