def is_over(r, c, n, m):
    if r < -(n // 2) or r > (n // 2) or c < -(m // 2) or c > (m // 2):
        return True
    else:
        return False


def move(keyinput, n, m, r, c, dir):
    nr = r + dir[keyinput][0]
    nc = c + dir[keyinput][1]
    if is_over(nr, nc, n, m):
        return (r, c)
    else:
        return (nr, nc)
    

def solution(keyinput, board):
    answer = [0, 0]
    dir = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    for k in keyinput:
        answer[0], answer[1] = move(k, board[0], board[1], answer[0], answer[1], dir)
    
    return answer