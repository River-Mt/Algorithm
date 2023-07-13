import sys
import heapq
from collections import deque
input = sys.stdin.readline

# 맨 처음 칸은 올리는 위치, 맨 마지막 칸은 내리는 위치
# 로봇은 오른쪽으로 이동, 이동 시 도착하는 칸의 내구도가 1감소
# 움직일 칸의 내구도가 0 이하라면 이동하지 않는다.


def solution():
    n, k = map(int, input().split())
    belt = deque(list(map(int, input().split())))
    robots = deque([0 for _ in range(n)])
    lev = 1

    def rotate_belt():
        belt.appendleft(belt.pop())
        robots.pop()
        robots.appendleft(0)
        if robots[-1] == 1:
            robots[-1] = 0

    def move_robot():
        for i in range(n-2, -1, -1):
            if robots[i] == 1:
                if robots[i + 1] != 1 and belt[i + 1] >= 1:
                    robots[i] = 0
                    robots[i + 1] = 1
                    belt[i + 1] -= 1

    def load_robot():
        if belt[0] == 0:
            return
        robots[0] = 1
        belt[0] -= 1

    def is_exit():
        return True if belt.count(0) >= k else False

    while True:
        # Step1
        rotate_belt()
        # Step2
        move_robot()
        # Step3
        load_robot()
        # Step4
        if is_exit():
            return lev

        lev += 1


print(solution())
