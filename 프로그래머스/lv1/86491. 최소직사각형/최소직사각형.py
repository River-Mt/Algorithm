def solution(sizes):
    answer = 0
    max_r = 0
    max_c = 0
    
    for r, c in sizes:
        if c < r:
            c, r = r, c
        max_r = max(r, max_r)
        max_c = max(c, max_c)
    
    return max_r * max_c