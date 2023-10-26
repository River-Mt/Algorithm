from collections import deque
def solution(n, lost, reserve):
    chk = set()
    for l in lost:
        if l in reserve:
            continue
        chk.add(l)
    
    for r in sorted(reserve):
        if r in lost:
            continue
        if r - 1 in chk:
            chk.remove(r-1)
        elif r + 1 in chk:
            chk.remove(r+1)
    
    return n - len(chk)