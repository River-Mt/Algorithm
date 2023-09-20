def solution(brown, yellow):
    for r in range(2503):
        c = brown // 2 - r + 2
        if (r-2) * (c-2) == yellow:
            return [max(r, c), min(r, c)]
        
    return[-1, -1]