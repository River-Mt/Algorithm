import sys
from collections import deque

q = deque()
dic = {}
m = int(sys.stdin.readline().rstrip())
xor = 0
hap = 0

for i in range(m):
    data = list(map(int, sys.stdin.readline().split()))

    if data[0] == 1:
        hap += data[1]
        xor = xor ^ data[1]
        q.append(data[1])
    elif data[0] == 2:
        hap -= data[1]
        xor = xor ^ data[1]
    elif data[0] == 3:
        print(hap)
    else:
        print(xor)
