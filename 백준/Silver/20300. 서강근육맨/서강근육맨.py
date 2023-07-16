import sys
from collections import deque
input = sys.stdin.readline


# 1번의 PT를 받을 때 운동기구를 최대 2개 선택 가능
# N개의 운동기구를 모두 사용해야하고 되도록이면 2개를 사용하려 함
# 운동기구는 각각 근손실 정도가 다름, PT를 한 번 받을 때 근손실 정도의 최솟값을 구해야 함
def solve():
    n = int(input().rstrip())
    q = deque(sorted(list(map(int, input().split()))))
    ans = 0
    if n % 2:
        ans = q.pop()

    while q:
        ans = max(q.pop() + q.popleft(), ans)

    return ans


print(solve())
