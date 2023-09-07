def solution(m, n, puddles):
    mod = 1000000007
    
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    
    def get_dp(r, c):
        if r == 1 and c == 1:
            return 1
        
        if r < 1 or c < 1 or [c, r] in puddles:
            return 0
        
        if dp[r][c] != -1:
            return dp[r][c]
        
        dp[r][c] = (get_dp(r-1, c) + get_dp(r, c-1))
        
        return dp[r][c] % mod
    
    answer = get_dp(n, m)
    
    return answer