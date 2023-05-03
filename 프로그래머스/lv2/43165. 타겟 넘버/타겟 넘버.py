def dfs(numbers, target, now, hap, size):
    if now >= size:
        if hap == target:
            return 1
        return 0
    
    ret = 0
    
    ret += dfs(numbers, target, now + 1, hap + numbers[now], size)
    ret += dfs(numbers, target, now + 1, hap - numbers[now], size)
    
    return ret
    

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0, len(numbers))
    return answer