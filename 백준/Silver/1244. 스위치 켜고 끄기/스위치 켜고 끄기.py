import sys

n = int(sys.stdin.readline().rstrip())
switches = list(map(int, sys.stdin.readline().split()))
stu = int(sys.stdin.readline().rstrip())


def change_state(sex, num):
    if sex == 1:
        for i in range(n):
            if (i + 1) % num == 0:
                switches[i] = switches[i] ^ 1
    else:
        l = num - 2
        r = num
        switches[num - 1] = switches[num - 1] ^ 1
        while l >= 0 and r < n:
            if switches[l] == switches[r]:
                switches[l] = switches[l] ^ 1
                switches[r] = switches[r] ^ 1
                l -= 1
                r += 1
            else:
                break


for i in range(stu):
    # if sex == 1 : male , else : female
    sex, num = map(int, sys.stdin.readline().split())
    change_state(sex, num)

for i in range(1, len(switches) + 1):
    print(switches[i - 1], end=" ")
    if i % 20 == 0:
        print()
