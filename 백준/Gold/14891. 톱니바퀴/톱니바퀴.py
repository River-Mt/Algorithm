gears = []

for i in range(4):
    gears.append(list(map(int, input().rstrip())))

k = int(input())


def check_rotate_gears(gear_num, d):
    idx = gear_num
    cur_d = d
    rotates = [0] * 4

    while idx >= 1:
        if gears[idx][6] == gears[idx - 1][2]:
            for i in range(idx):
                rotates[i] = 0
            break
        cur_d *= -1
        rotates[idx - 1] = cur_d
        idx -= 1

    idx = gear_num
    cur_d = d

    while idx < 3:
        if gears[idx][2] == gears[idx + 1][6]:
            for i in range(idx + 1, 4):
                rotates[i] = 0
            break
        cur_d *= -1
        rotates[idx + 1] = cur_d
        idx += 1

    rotates[gear_num] = d

    return rotates


def cw(gear):
    last = gear[7]
    idx = 7
    while idx >= 1:
        gear[idx] = gear[idx - 1]
        idx -= 1
    gear[0] = last
    return


def ccw(gear):
    head = gear[0]

    for i in range(1, 8):
        gear[i - 1] = gear[i]

    gear[7] = head

    return


def rotate_gears(rotates):
    for i in range(4):
        d = rotates[i]
        if d == 1:
            cw(gears[i])
        elif d == -1:
            ccw(gears[i])


def get_score():
    ret = 0
    for i in range(len(gears)):
        if gears[i][0] == 1:
            ret += 2 ** i
    return ret


for i in range(k):
    num, d = map(int, input().split())
    rotate_gears(check_rotate_gears(num - 1, d))

print(get_score())
